const https = require('https');
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const baseUrl = 'https://brooksfloorcovering.com';
const assetsDir = 'assets/original';

// Create necessary directories
['images', 'css', 'js'].forEach(dir => {
    fs.mkdirSync(path.join(assetsDir, dir), { recursive: true });
});

function isValidFile(url) {
    const ext = path.extname(url).toLowerCase();
    const validExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.css', '.js'];
    return validExtensions.includes(ext);
}

function downloadFile(url, localPath) {
    return new Promise((resolve, reject) => {
        https.get(url, response => {
            if (response.statusCode !== 200) {
                reject(new Error(`Failed to download ${url}: ${response.statusCode}`));
                return;
            }

            const fileStream = fs.createWriteStream(localPath);
            response.pipe(fileStream);

            fileStream.on('finish', () => {
                fileStream.close();
                console.log(`Successfully downloaded ${path.basename(localPath)}`);
                resolve();
            });

            fileStream.on('error', err => {
                fs.unlink(localPath, () => {});
                reject(err);
            });
        }).on('error', err => {
            reject(err);
        });
    });
}

async function main() {
    try {
        // First install jsdom
        console.log('Installing jsdom...');
        require('child_process').execSync('npm install jsdom', { stdio: 'inherit' });

        console.log('Fetching main page...');
        const response = await new Promise((resolve, reject) => {
            https.get(baseUrl, res => {
                let data = '';
                res.on('data', chunk => data += chunk);
                res.on('end', () => resolve(data));
                res.on('error', reject);
            });
        });

        const dom = new JSDOM(response);
        const document = dom.window.document;

        // Find all assets
        const assets = [
            ...Array.from(document.querySelectorAll('img')).map(img => ({ url: img.src, type: 'images' })),
            ...Array.from(document.querySelectorAll('link[rel="stylesheet"]')).map(link => ({ url: link.href, type: 'css' })),
            ...Array.from(document.querySelectorAll('script[src]')).map(script => ({ url: script.src, type: 'js' }))
        ];

        // Download each asset
        for (const asset of assets) {
            if (!asset.url) continue;

            const fullUrl = new URL(asset.url, baseUrl).href;
            if (!isValidFile(fullUrl)) continue;

            const filename = path.basename(new URL(fullUrl).pathname);
            if (!filename) continue;

            const localPath = path.join(assetsDir, asset.type, filename);
            
            console.log(`Downloading ${fullUrl} to ${localPath}`);
            try {
                await downloadFile(fullUrl, localPath);
            } catch (err) {
                console.error(`Failed to download ${filename}: ${err.message}`);
            }
        }

        console.log('Asset download complete!');
    } catch (err) {
        console.error('Error:', err);
        process.exit(1);
    }
}

main();
