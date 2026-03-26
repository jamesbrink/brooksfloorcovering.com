/** Metadata for a service-area city landing page. */
export interface ServiceArea {
  city: string;
  slug: string;
  tagline: string;
  description: string;
  neighborhoods: string[];
  popularServices: string[];
  highlight?: boolean;
}

export const serviceAreas: ServiceArea[] = [
  {
    city: 'Phoenix',
    slug: 'phoenix',
    tagline: 'Heart of the Valley',
    description:
      'As the heart of the Valley, Phoenix is where we complete the most projects each year. From historic neighborhoods like Arcadia and Encanto to newer developments in Laveen, Ahwatukee, and Desert Ridge, our team installs flooring in homes and businesses across every corner of the city. Whether you need tile for a midtown restaurant or carpet for a North Phoenix office park, we know this market inside and out.',
    neighborhoods: ['Arcadia', 'Encanto', 'Ahwatukee', 'Desert Ridge', 'Laveen', 'North Phoenix'],
    popularServices: ['Tile', 'Carpet', 'LVP'],
  },
  {
    city: 'Scottsdale',
    slug: 'scottsdale',
    tagline: 'Luxury Flooring Specialists',
    description:
      "Scottsdale homeowners and business owners expect premium quality, and we deliver it. We have completed projects in Old Town Scottsdale boutiques, Gainey Ranch estates, DC Ranch residences, and resort properties throughout the city. Our experience with high-end tile, natural stone, and engineered hardwood makes us a trusted partner for Scottsdale's luxury flooring market.",
    neighborhoods: ['Old Town', 'Gainey Ranch', 'DC Ranch', 'North Scottsdale'],
    popularServices: ['Natural Stone', 'Engineered Hardwood', 'Custom Tile'],
  },
  {
    city: 'Mesa',
    slug: 'mesa',
    tagline: 'East Valley Coverage',
    description:
      'Mesa is one of the fastest-growing cities in Arizona, and we have been installing flooring here for decades. From family homes near Fiesta Mall and Red Mountain Ranch to commercial spaces along the US-60 corridor and Mesa Gateway area, our team provides professional installation, concrete polishing, and floor preparation services throughout the city.',
    neighborhoods: ['Red Mountain Ranch', 'Mesa Gateway', 'Superstition Springs'],
    popularServices: ['Polished Concrete', 'Floor Preparation', 'Tile'],
  },
  {
    city: 'Chandler',
    slug: 'chandler',
    tagline: 'Tech Corridor & Beyond',
    description:
      "Chandler's mix of tech campuses, shopping centers, and master-planned communities keeps our team busy year-round. We regularly work in neighborhoods like Ocotillo, Sun Groves, and Chandler Heights, as well as commercial spaces near Chandler Fashion Center and the Price Road corridor. LVP, tile, and polished concrete are popular choices for Chandler clients.",
    neighborhoods: ['Ocotillo', 'Sun Groves', 'Chandler Heights', 'Price Corridor'],
    popularServices: ['LVP', 'Tile', 'Polished Concrete'],
  },
  {
    city: 'Tempe',
    slug: 'tempe',
    tagline: 'Urban & University District',
    description:
      'Home to Arizona State University and a thriving business district, Tempe has a unique mix of student housing, condos, restaurants, and corporate offices. We install flooring for property managers near Mill Avenue, homeowners in South Tempe, and commercial tenants throughout the Tempe Marketplace and Rio Salado areas.',
    neighborhoods: ['Mill Avenue', 'South Tempe', 'Tempe Marketplace', 'Rio Salado'],
    popularServices: ['LVP', 'Carpet', 'Epoxy'],
  },
  {
    city: 'Gilbert',
    slug: 'gilbert',
    tagline: 'Family-Friendly Communities',
    description:
      "Gilbert has grown from a small farming town to one of the Valley's most desirable communities. We serve homeowners in Agritopia, Val Vista Lakes, Power Ranch, and the Heritage District with carpet, hardwood, tile, and luxury vinyl plank installations. Our residential flooring services are a perfect fit for Gilbert's family-friendly neighborhoods.",
    neighborhoods: ['Agritopia', 'Val Vista Lakes', 'Power Ranch', 'Heritage District'],
    popularServices: ['Carpet', 'Hardwood', 'LVP'],
  },
  {
    city: 'Glendale',
    slug: 'glendale',
    tagline: 'Our Home Base',
    description:
      'Glendale is our home base, and we are proud to serve the community where our business was built. From the Westgate Entertainment District and State Farm Stadium area to established neighborhoods near downtown and Arrowhead Ranch, we handle residential and commercial flooring projects of every size. Our proximity means faster response times and deep knowledge of the local market.',
    neighborhoods: ['Westgate', 'Arrowhead Ranch', 'Downtown', 'State Farm Stadium Area'],
    popularServices: ['Carpet', 'Tile', 'LVP', 'Epoxy'],
    highlight: true,
  },
  {
    city: 'Peoria',
    slug: 'peoria',
    tagline: 'West Valley to Lake Pleasant',
    description:
      'Peoria stretches from the heart of the West Valley to the foothills of Lake Pleasant, and we serve every part of it. Our team installs flooring in homes near Vistancia, Westwing, and the P83 entertainment district, as well as commercial properties along Grand Avenue and the Bell Road corridor. Tile, epoxy, and carpet are popular choices for Peoria clients.',
    neighborhoods: ['Vistancia', 'Westwing', 'P83 District'],
    popularServices: ['Tile', 'Epoxy', 'Carpet'],
  },
  {
    city: 'Surprise',
    slug: 'surprise',
    tagline: 'New Construction Experts',
    description:
      'Surprise has seen tremendous growth over the past decade, and we have been part of it. From Sun City Grand and Marley Park to new construction near Prasada and the Surprise City Center, we provide flooring installation for homes and businesses throughout the community. Our experience with new-build installations makes us a valuable partner for Surprise homeowners and builders alike.',
    neighborhoods: ['Sun City Grand', 'Marley Park', 'Prasada', 'Surprise City Center'],
    popularServices: ['LVP', 'Tile', 'Carpet'],
  },
  {
    city: 'Goodyear',
    slug: 'goodyear',
    tagline: 'Master-Planned Communities',
    description:
      "Goodyear's master-planned communities and expanding commercial districts create steady demand for professional flooring services. We work in Estrella Mountain Ranch, Palm Valley, Pebble Creek, and Canyon Trails, installing everything from luxury vinyl plank and carpet to tile and polished concrete. Our team is familiar with the products and styles that Goodyear homeowners prefer.",
    neighborhoods: ['Estrella Mountain Ranch', 'Palm Valley', 'Pebble Creek', 'Canyon Trails'],
    popularServices: ['LVP', 'Carpet', 'Polished Concrete'],
  },
  {
    city: 'Avondale',
    slug: 'avondale',
    tagline: 'I-10 Corridor',
    description:
      'Located along the I-10 corridor between Phoenix and Goodyear, Avondale is a growing community with a mix of residential neighborhoods and commercial developments. We serve homeowners in Coldwater Springs, Garden Lakes, and Crystal Gardens, as well as businesses near Avondale Boulevard. Carpet, tile, and LVP installations are our most requested services in the area.',
    neighborhoods: ['Coldwater Springs', 'Garden Lakes', 'Crystal Gardens'],
    popularServices: ['Carpet', 'Tile', 'LVP'],
  },
  {
    city: 'Buckeye',
    slug: 'buckeye',
    tagline: 'Fastest-Growing City in AZ',
    description:
      "Buckeye is one of the fastest-growing cities in Arizona, with new homes and commercial developments expanding rapidly to the west. We provide flooring services in Verrado, Sundance, Tartesso, and Festival Ranch, as well as commercial projects along the MC 85 and I-10 corridors. Whether it's a brand-new home or a commercial build-out, our team delivers quality results.",
    neighborhoods: ['Verrado', 'Sundance', 'Tartesso', 'Festival Ranch'],
    popularServices: ['LVP', 'Tile', 'Carpet'],
  },
];
