/** A single question-and-answer pair for a city landing page. */
export interface ServiceAreaFaq {
  question: string;
  answer: string;
}

/** Metadata for a service-area city landing page. */
export interface ServiceArea {
  city: string;
  slug: string;
  tagline: string;
  description: string;
  neighborhoods: string[];
  popularServices: string[];
  faqs: ServiceAreaFaq[];
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
    faqs: [
      {
        question: 'Do you install flooring in Arcadia and Ahwatukee?',
        answer:
          'Yes. We work throughout Phoenix, including Arcadia, Encanto, Ahwatukee, Desert Ridge, Laveen, and North Phoenix. Phoenix is where we complete the most projects each year, so our crews know these neighborhoods and their homes well.',
      },
      {
        question: 'What flooring works best for Phoenix homes?',
        answer:
          'Tile and luxury vinyl plank are two of our most requested options in Phoenix because they stand up to heat, foot traffic, and everyday wear. Carpet remains a favorite for bedrooms and living areas where comfort matters. We help you weigh the options for each room during a free estimate.',
      },
      {
        question: 'Are you licensed to work in Phoenix?',
        answer:
          'We are fully licensed, bonded, and insured under Arizona ROC #226840, which covers work statewide, including all of Phoenix. Brooks Floor Covering has served the Valley since 1994 as a family-owned business.',
      },
      {
        question: 'How do estimates work for Phoenix projects?',
        answer:
          'Every Phoenix project begins with a free, no-obligation estimate. We visit your home or business, measure the space, discuss materials, and provide a written estimate. Call (623) 688-8422 to schedule.',
      },
      {
        question: 'Do you handle both homes and businesses in Phoenix?',
        answer:
          'Yes. We install flooring for Phoenix homeowners and for commercial spaces such as offices, retail stores, and restaurants across the city. From a midtown storefront to an Ahwatukee living room, we bring the same professional installation to every job.',
      },
    ],
  },
  {
    city: 'Scottsdale',
    slug: 'scottsdale',
    tagline: 'Luxury Flooring Specialists',
    description:
      "Scottsdale homeowners and business owners expect premium quality, and we deliver it. We have completed projects in Old Town Scottsdale boutiques, Gainey Ranch estates, DC Ranch residences, and resort properties throughout the city. Our experience with high-end tile, natural stone, and engineered hardwood makes us a trusted partner for Scottsdale's luxury flooring market.",
    neighborhoods: ['Old Town', 'Gainey Ranch', 'DC Ranch', 'North Scottsdale'],
    popularServices: ['Natural Stone', 'Engineered Hardwood', 'Custom Tile'],
    faqs: [
      {
        question: 'Do you install flooring in Gainey Ranch and DC Ranch?',
        answer:
          'Yes. We serve all of Scottsdale, including Old Town, Gainey Ranch, DC Ranch, and North Scottsdale. Our experience with high-end tile, natural stone, and engineered hardwood is a good match for the area.',
      },
      {
        question: 'What flooring works best for Scottsdale homes?',
        answer:
          'Natural stone, engineered hardwood, and custom tile are our most requested finishes in Scottsdale because they suit the area’s upscale interiors. We help you choose materials that fit your design and hold up to daily use during a free estimate.',
      },
      {
        question: 'Can you do custom tile and shower work in Scottsdale?',
        answer:
          'Absolutely. Custom tile is one of our most popular Scottsdale services, and we build complete custom tile showers with proper waterproofing and precise layouts. We also handle backsplashes, feature walls, and detailed accent work.',
      },
      {
        question: 'Are you licensed to work in Scottsdale?',
        answer:
          'Yes. Brooks Floor Covering is licensed, bonded, and insured under Arizona ROC #226840, which is valid statewide, including Scottsdale. We have been a family-owned business serving the Valley since 1994.',
      },
      {
        question: 'How do estimates work for Scottsdale projects?',
        answer:
          'Every Scottsdale project starts with a free, no-obligation estimate. We visit your home or property, review materials and layout, and provide a written estimate with no pressure. Call (623) 688-8422 to set up a visit.',
      },
    ],
  },
  {
    city: 'Mesa',
    slug: 'mesa',
    tagline: 'East Valley Coverage',
    description:
      'Mesa is one of the fastest-growing cities in Arizona, and we have been installing flooring here for decades. From family homes near Fiesta Mall and Red Mountain Ranch to commercial spaces along the US-60 corridor and Mesa Gateway area, our team provides professional installation, concrete polishing, and floor preparation services throughout the city.',
    neighborhoods: ['Red Mountain Ranch', 'Mesa Gateway', 'Superstition Springs'],
    popularServices: ['Polished Concrete', 'Floor Preparation', 'Tile'],
    faqs: [
      {
        question: 'Do you install flooring in Red Mountain Ranch and Superstition Springs?',
        answer:
          'Yes. We serve all of Mesa, including Red Mountain Ranch, Mesa Gateway, and Superstition Springs. We have been installing flooring in Mesa for decades and know the area’s homes and commercial spaces well.',
      },
      {
        question: 'What flooring works best for Mesa homes and businesses?',
        answer:
          'Polished concrete, floor preparation, and tile are our most requested Mesa services. Polished concrete is a durable, low-maintenance choice for commercial spaces along the US-60 corridor, while tile is a lasting option for family homes.',
      },
      {
        question: 'Do you offer concrete polishing and floor prep in Mesa?',
        answer:
          'Yes. Concrete polishing and floor preparation are two of our specialties in Mesa. We handle grinding, moisture mitigation, leveling, and subfloor prep so your finished floor is built to last.',
      },
      {
        question: 'Are you licensed to work in Mesa?',
        answer:
          'We are licensed, bonded, and insured under Arizona ROC #226840, which covers work throughout the state, including Mesa. Brooks Floor Covering has been family-owned and serving the Valley since 1994.',
      },
      {
        question: 'How do estimates work for Mesa projects?',
        answer:
          'Every Mesa project starts with a free, no-obligation estimate. We visit the site, assess the space and subfloor, and provide a written estimate. Call (623) 688-8422 to schedule.',
      },
    ],
  },
  {
    city: 'Chandler',
    slug: 'chandler',
    tagline: 'Tech Corridor & Beyond',
    description:
      "Chandler's mix of tech campuses, shopping centers, and master-planned communities keeps our team busy year-round. We regularly work in neighborhoods like Ocotillo, Sun Groves, and Chandler Heights, as well as commercial spaces near Chandler Fashion Center and the Price Road corridor. LVP, tile, and polished concrete are popular choices for Chandler clients.",
    neighborhoods: ['Ocotillo', 'Sun Groves', 'Chandler Heights', 'Price Corridor'],
    popularServices: ['LVP', 'Tile', 'Polished Concrete'],
    faqs: [
      {
        question: 'Do you install flooring in Ocotillo and Chandler Heights?',
        answer:
          'Yes. We regularly work in Ocotillo, Sun Groves, Chandler Heights, and the Price Corridor. Chandler’s mix of master-planned communities and tech campuses keeps our crews busy here year-round.',
      },
      {
        question: 'What flooring works best for Chandler homes?',
        answer:
          'Luxury vinyl plank, tile, and polished concrete are our most popular Chandler choices. LVP is waterproof and scratch-resistant for busy households, while tile and polished concrete suit both homes and commercial spaces near Chandler Fashion Center.',
      },
      {
        question: 'Do you handle commercial flooring near the Price Corridor?',
        answer:
          'Yes. We install flooring for offices, retail, and other commercial spaces along the Price Road corridor and throughout Chandler. Polished concrete and tile are frequent choices for these projects.',
      },
      {
        question: 'Are you licensed to work in Chandler?',
        answer:
          'We are licensed, bonded, and insured under Arizona ROC #226840, which is valid statewide, including Chandler. Brooks Floor Covering has been a family-owned business serving the Valley since 1994.',
      },
      {
        question: 'How do estimates work for Chandler projects?',
        answer:
          'Every Chandler project begins with a free, no-obligation estimate. We measure your space, review materials, and give you a written estimate with no pressure. Call (623) 688-8422 to schedule.',
      },
    ],
  },
  {
    city: 'Tempe',
    slug: 'tempe',
    tagline: 'Urban & University District',
    description:
      'Home to Arizona State University and a thriving business district, Tempe has a unique mix of student housing, condos, restaurants, and corporate offices. We install flooring for property managers near Mill Avenue, homeowners in South Tempe, and commercial tenants throughout the Tempe Marketplace and Rio Salado areas.',
    neighborhoods: ['Mill Avenue', 'South Tempe', 'Tempe Marketplace', 'Rio Salado'],
    popularServices: ['LVP', 'Carpet', 'Epoxy'],
    faqs: [
      {
        question: 'Do you install flooring near Mill Avenue and South Tempe?',
        answer:
          'Yes. We serve all of Tempe, including Mill Avenue, South Tempe, Tempe Marketplace, and Rio Salado. We work with homeowners, property managers, and commercial tenants across the city.',
      },
      {
        question: 'What flooring works best for Tempe rentals and homes?',
        answer:
          'Luxury vinyl plank and carpet are popular Tempe choices, especially for student housing, condos, and rentals where durability and easy maintenance matter. Epoxy is a frequent pick for commercial and garage floors near the Rio Salado area.',
      },
      {
        question: 'Do you work with property managers on Tempe units?',
        answer:
          'Yes. We install flooring for property managers and landlords throughout Tempe, from single units near Mill Avenue to larger multi-unit turnovers. We handle both residential and commercial work.',
      },
      {
        question: 'Are you licensed to work in Tempe?',
        answer:
          'We are licensed, bonded, and insured under Arizona ROC #226840, valid statewide, including Tempe. Brooks Floor Covering has been family-owned and serving the Valley since 1994.',
      },
      {
        question: 'How do estimates work for Tempe projects?',
        answer:
          'Every Tempe project starts with a free, no-obligation estimate. We visit the property, measure, and provide a written estimate. Call (623) 688-8422 to schedule a visit.',
      },
    ],
  },
  {
    city: 'Gilbert',
    slug: 'gilbert',
    tagline: 'Family-Friendly Communities',
    description:
      "Gilbert has grown from a small farming town to one of the Valley's most desirable communities. We serve homeowners in Agritopia, Val Vista Lakes, Power Ranch, and the Heritage District with carpet, hardwood, tile, and luxury vinyl plank installations. Our residential flooring services are a perfect fit for Gilbert's family-friendly neighborhoods.",
    neighborhoods: ['Agritopia', 'Val Vista Lakes', 'Power Ranch', 'Heritage District'],
    popularServices: ['Carpet', 'Hardwood', 'LVP'],
    faqs: [
      {
        question: 'Do you install flooring in Agritopia and Power Ranch?',
        answer:
          'Yes. We serve homeowners throughout Gilbert, including Agritopia, Val Vista Lakes, Power Ranch, and the Heritage District. Our residential services are a natural fit for Gilbert’s family-friendly neighborhoods.',
      },
      {
        question: 'What flooring works best for Gilbert homes?',
        answer:
          'Carpet, hardwood, and luxury vinyl plank are our most requested Gilbert options. Carpet adds comfort to bedrooms, engineered hardwood brings warmth to living spaces, and LVP offers a durable, waterproof choice for busy family areas.',
      },
      {
        question: 'Do you install engineered and solid hardwood in Gilbert?',
        answer:
          'Yes. Hardwood is one of our popular Gilbert services, and we install oak, maple, hickory, walnut, and exotic species in engineered and solid formats. We help you pick the right product for your home during a free estimate.',
      },
      {
        question: 'Are you licensed to work in Gilbert?',
        answer:
          'We are licensed, bonded, and insured under Arizona ROC #226840, which is valid statewide, including Gilbert. Brooks Floor Covering has been a family-owned business serving the Valley since 1994.',
      },
      {
        question: 'How do estimates work for Gilbert projects?',
        answer:
          'Every Gilbert project starts with a free, no-obligation estimate. We measure your rooms, review flooring options, and provide a written estimate. Call (623) 688-8422 to schedule.',
      },
    ],
  },
  {
    city: 'Glendale',
    slug: 'glendale',
    tagline: 'Our Home Base',
    description:
      'Glendale is our home base, and we are proud to serve the community where our business was built. From the Westgate Entertainment District and State Farm Stadium area to established neighborhoods near downtown and Arrowhead Ranch, we handle residential and commercial flooring projects of every size. Our proximity means faster response times and deep knowledge of the local market.',
    neighborhoods: ['Westgate', 'Arrowhead Ranch', 'Downtown', 'State Farm Stadium Area'],
    popularServices: ['Carpet', 'Tile', 'LVP', 'Epoxy'],
    faqs: [
      {
        question: 'Do you install flooring in Arrowhead Ranch and the Westgate area?',
        answer:
          'Yes. Glendale is our home base, so we work throughout the city, including Westgate, Arrowhead Ranch, downtown, and the State Farm Stadium area. Being local means faster response times and deep knowledge of the market.',
      },
      {
        question: 'What flooring works best for Glendale homes and businesses?',
        answer:
          'Carpet, tile, luxury vinyl plank, and epoxy are our most requested Glendale services. Carpet and LVP suit homes near Arrowhead Ranch, while tile and epoxy are durable choices for commercial spaces around the Westgate Entertainment District.',
      },
      {
        question: 'Are you based in Glendale?',
        answer:
          'Yes. Glendale is where our family business was built, and we are proud to serve the community that has supported us since 1994. Our proximity means quicker scheduling and a strong understanding of local homes and businesses.',
      },
      {
        question: 'Are you licensed to work in Glendale?',
        answer:
          'We are licensed, bonded, and insured under Arizona ROC #226840, which is valid statewide, including Glendale. Brooks Floor Covering handles residential and commercial projects of every size.',
      },
      {
        question: 'How do estimates work for Glendale projects?',
        answer:
          'Every Glendale project starts with a free, no-obligation estimate. As your local flooring company, we can often visit quickly, measure your space, and provide a written estimate. Call (623) 688-8422 to schedule.',
      },
    ],
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
    faqs: [
      {
        question: 'Do you install flooring in Vistancia and Westwing?',
        answer:
          'Yes. We serve all of Peoria, from Vistancia and Westwing to the P83 entertainment district and the Lake Pleasant foothills. We handle homes and commercial properties across the city.',
      },
      {
        question: 'What flooring works best for Peoria homes?',
        answer:
          'Tile, epoxy, and carpet are our most requested Peoria choices. Tile holds up well to heat and traffic, epoxy is a durable option for garages and commercial floors, and carpet adds comfort to living spaces.',
      },
      {
        question: 'Do you install epoxy garage and commercial floors in Peoria?',
        answer:
          'Yes. Epoxy is one of our popular Peoria services. We apply seamless, durable coatings ideal for garages, warehouses, and commercial spaces along Grand Avenue and the Bell Road corridor.',
      },
      {
        question: 'Are you licensed to work in Peoria?',
        answer:
          'We are licensed, bonded, and insured under Arizona ROC #226840, valid statewide, including Peoria. Brooks Floor Covering has been a family-owned business serving the Valley since 1994.',
      },
      {
        question: 'How do estimates work for Peoria projects?',
        answer:
          'Every Peoria project starts with a free, no-obligation estimate. We visit your home or business, measure, and provide a written estimate. Call (623) 688-8422 to schedule.',
      },
    ],
  },
  {
    city: 'Surprise',
    slug: 'surprise',
    tagline: 'New Construction Experts',
    description:
      'Surprise has seen tremendous growth over the past decade, and we have been part of it. From Sun City Grand and Marley Park to new construction near Prasada and the Surprise City Center, we provide flooring installation for homes and businesses throughout the community. Our experience with new-build installations makes us a valuable partner for Surprise homeowners and builders alike.',
    neighborhoods: ['Sun City Grand', 'Marley Park', 'Prasada', 'Surprise City Center'],
    popularServices: ['LVP', 'Tile', 'Carpet'],
    faqs: [
      {
        question: 'Do you install flooring in Sun City Grand and Marley Park?',
        answer:
          'Yes. We serve all of Surprise, including Sun City Grand, Marley Park, Prasada, and the Surprise City Center. We work with homeowners and builders throughout the community.',
      },
      {
        question: 'What flooring works best for Surprise homes?',
        answer:
          'Luxury vinyl plank, tile, and carpet are our most requested Surprise choices. LVP is waterproof and low-maintenance, tile stands up to the heat, and carpet keeps bedrooms and living areas comfortable.',
      },
      {
        question: 'Do you work on new construction in Surprise?',
        answer:
          'Yes. New-build installation is one of our strengths in Surprise, where we have worked through years of steady growth near Prasada and the Surprise City Center. We partner with homeowners and builders on new homes and businesses.',
      },
      {
        question: 'Are you licensed to work in Surprise?',
        answer:
          'We are licensed, bonded, and insured under Arizona ROC #226840, which is valid statewide, including Surprise. Brooks Floor Covering has been family-owned and serving the Valley since 1994.',
      },
      {
        question: 'How do estimates work for Surprise projects?',
        answer:
          'Every Surprise project starts with a free, no-obligation estimate. We measure the space, review options, and provide a written estimate. Call (623) 688-8422 to schedule.',
      },
    ],
  },
  {
    city: 'Goodyear',
    slug: 'goodyear',
    tagline: 'Master-Planned Communities',
    description:
      "Goodyear's master-planned communities and expanding commercial districts create steady demand for professional flooring services. We work in Estrella Mountain Ranch, Palm Valley, Pebble Creek, and Canyon Trails, installing everything from luxury vinyl plank and carpet to tile and polished concrete. Our team is familiar with the products and styles that Goodyear homeowners prefer.",
    neighborhoods: ['Estrella Mountain Ranch', 'Palm Valley', 'Pebble Creek', 'Canyon Trails'],
    popularServices: ['LVP', 'Carpet', 'Polished Concrete'],
    faqs: [
      {
        question: 'Do you install flooring in Estrella Mountain Ranch and Palm Valley?',
        answer:
          'Yes. We serve all of Goodyear, including Estrella Mountain Ranch, Palm Valley, Pebble Creek, and Canyon Trails. Goodyear’s master-planned communities keep our crews busy across the city.',
      },
      {
        question: 'What flooring works best for Goodyear homes?',
        answer:
          'Luxury vinyl plank, carpet, and polished concrete are our most requested Goodyear choices. LVP and carpet suit family homes in Palm Valley and Pebble Creek, while polished concrete is a durable pick for commercial and modern spaces.',
      },
      {
        question: 'Do you offer polished concrete in Goodyear?',
        answer:
          'Yes. Polished concrete is a popular Goodyear service. We transform raw concrete into a sleek, low-maintenance finished floor in anything from a matte to a high-gloss look, for homes and commercial properties alike.',
      },
      {
        question: 'Are you licensed to work in Goodyear?',
        answer:
          'We are licensed, bonded, and insured under Arizona ROC #226840, valid statewide, including Goodyear. Brooks Floor Covering has been a family-owned business serving the Valley since 1994.',
      },
      {
        question: 'How do estimates work for Goodyear projects?',
        answer:
          'Every Goodyear project starts with a free, no-obligation estimate. We visit your home or business, measure, and provide a written estimate. Call (623) 688-8422 to schedule.',
      },
    ],
  },
  {
    city: 'Avondale',
    slug: 'avondale',
    tagline: 'I-10 Corridor',
    description:
      'Located along the I-10 corridor between Phoenix and Goodyear, Avondale is a growing community with a mix of residential neighborhoods and commercial developments. We serve homeowners in Coldwater Springs, Garden Lakes, and Crystal Gardens, as well as businesses near Avondale Boulevard. Carpet, tile, and LVP installations are our most requested services in the area.',
    neighborhoods: ['Coldwater Springs', 'Garden Lakes', 'Crystal Gardens'],
    popularServices: ['Carpet', 'Tile', 'LVP'],
    faqs: [
      {
        question: 'Do you install flooring in Coldwater Springs and Garden Lakes?',
        answer:
          'Yes. We serve all of Avondale, including Coldwater Springs, Garden Lakes, and Crystal Gardens. We handle both homes and businesses along the I-10 corridor and throughout the city.',
      },
      {
        question: 'What flooring works best for Avondale homes?',
        answer:
          'Carpet, tile, and luxury vinyl plank are our most requested Avondale choices. Carpet adds comfort to bedrooms, tile stands up to heat and traffic, and LVP is a durable, waterproof option for busy households.',
      },
      {
        question: 'Do you handle commercial flooring in Avondale?',
        answer:
          'Yes. We install flooring for businesses near Avondale Boulevard and across the city, in addition to our residential work. From offices to retail spaces, we bring the same professional installation to every project.',
      },
      {
        question: 'Are you licensed to work in Avondale?',
        answer:
          'We are licensed, bonded, and insured under Arizona ROC #226840, which is valid statewide, including Avondale. Brooks Floor Covering has been family-owned and serving the Valley since 1994.',
      },
      {
        question: 'How do estimates work for Avondale projects?',
        answer:
          'Every Avondale project starts with a free, no-obligation estimate. We measure your space, review options, and provide a written estimate. Call (623) 688-8422 to schedule.',
      },
    ],
  },
  {
    city: 'Buckeye',
    slug: 'buckeye',
    tagline: 'Fastest-Growing City in AZ',
    description:
      "Buckeye is one of the fastest-growing cities in Arizona, with new homes and commercial developments expanding rapidly to the west. We provide flooring services in Verrado, Sundance, Tartesso, and Festival Ranch, as well as commercial projects along the MC 85 and I-10 corridors. Whether it's a brand-new home or a commercial build-out, our team delivers quality results.",
    neighborhoods: ['Verrado', 'Sundance', 'Tartesso', 'Festival Ranch'],
    popularServices: ['LVP', 'Tile', 'Carpet'],
    faqs: [
      {
        question: 'Do you install flooring in Verrado and Festival Ranch?',
        answer:
          'Yes. We serve all of Buckeye, including Verrado, Sundance, Tartesso, and Festival Ranch. As one of Arizona’s fastest-growing cities, Buckeye keeps our crews busy with new homes and commercial build-outs.',
      },
      {
        question: 'What flooring works best for Buckeye homes?',
        answer:
          'Luxury vinyl plank, tile, and carpet are our most requested Buckeye choices. LVP is waterproof and durable for new homes, tile stands up to the heat, and carpet keeps living areas and bedrooms comfortable.',
      },
      {
        question: 'Do you work on new construction and build-outs in Buckeye?',
        answer:
          'Yes. We handle new homes and commercial build-outs across Buckeye, including projects along the MC 85 and I-10 corridors. Whether it is a brand-new home in Verrado or a commercial space, our team delivers quality results.',
      },
      {
        question: 'Are you licensed to work in Buckeye?',
        answer:
          'We are licensed, bonded, and insured under Arizona ROC #226840, valid statewide, including Buckeye. Brooks Floor Covering has been a family-owned business serving the Valley since 1994.',
      },
      {
        question: 'How do estimates work for Buckeye projects?',
        answer:
          'Every Buckeye project starts with a free, no-obligation estimate. We visit the site, measure, and provide a written estimate. Call (623) 688-8422 to schedule.',
      },
    ],
  },
];
