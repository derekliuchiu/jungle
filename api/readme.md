## API documentation

Base Url: `api.jungleapi.org`  
A valid API Key must be included as the `Authorization` header  

### Routes
Look up a product from its ASIN
`/product`
| Param | Description | Example |  
| ----------- | ----------- | ----------- |
| `asin` | Amazon product identifier | `B000YDDF6O` | 

Response:  
As much data as we can scrape from the site. Example:
```
{
  "title": "AKASO V50 Elite 4K60fps Touch Screen WiFi Action Camera Voice Control EIS 131 feet Waterproof Camera Adjustable View Angle 8X Zoom Remote Control Sports Camera with Helmet Accessories Kit",
  "bestsellers_rank": [
    {
      "category": "Electronics",
      "rank": 2341,
      "link": "https://www.amazon.com/gp/bestsellers/electronics/ref=pd_zg_ts_electronics"
    },
    {
      "category": "Underwater Photography Camcorders",
      "rank": 2,
      "link": "https://www.amazon.com/gp/bestsellers/electronics/3426471/ref=pd_zg_hrsr_electronics"
    }
  ],
  "brand": "AKASO",
  "weight": "1.2 pounds",
  "shipping_weight": "1.2 pounds",
  "first_available": {
    "raw": "October 17, 2018",
    "utc": "2018-10-16T23:00:00.000Z"
  },
  "dimensions": "2.4 x 1.6 x 1.2 inches",
  "link": "https://www.amazon.com/AKASO-Control-Waterproof-Adjustable-Accessories/dp/B07J4TNYV8",
  "sub_title": {
    "text": "AKASO",
    "link": "https://www.amazon.com/AKASO/b/ref=bl_dp_s_web_7188749011?ie=UTF8&node=7188749011&field-lbr_brands_browse-bin=AKASO"
  },
  "rating": 4.4,
  "ratings_total": 991,
  "reviews_total": 896,
  "main_image": {
    "link": "https://images-na.ssl-images-amazon.com/images/I/61j2gU3e6LL._SL1001_.jpg"
  },
  "images": [
    {
      "link": "https://images-na.ssl-images-amazon.com/images/I/41bv6NOh09L._SS40_.jpg"
    },
    {
      "link": "https://images-na.ssl-images-amazon.com/images/I/51l9lEoxhhL._SS40_.jpg"
    },
    {
      "link": "https://images-na.ssl-images-amazon.com/images/I/51%2B-OEaYxgL._SS40_.jpg"
    },
    {
      "link": "https://images-na.ssl-images-amazon.com/images/I/51sVMy0FesL._SS40_.jpg"
    },
    {
      "link": "https://images-na.ssl-images-amazon.com/images/I/51yBIOz02DL._SS40_.jpg"
    },
    {
      "link": "https://images-na.ssl-images-amazon.com/images/I/51JqYR4YPyL._SS40_.jpg"
    },
    {
      "link": "https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif"
    }
  ],
  "videos": [
    {
      "duration_seconds": 12,
      "width": 368,
      "height": 480,
      "link": "https://d12xgfa7l6zj5h.cloudfront.net/cdb29b94-8291-4b81-ad7b-31579d487af6/default.jobtemplate.mp4.480.mp4",
      "thumbnail": "https://images-na.ssl-images-amazon.com/images/I/71STGqZQgOL.SX522_.png",
      "is_hero_video": false,
      "variant": "MAIN"
    }
  ],
  "feature_bullets": [
    "UPGRADED SERIES OF AKASO V50: Records 4K/60fps, 4K/30fps, 2.7K/60fps, 2.7K/30fps, 1080P/120fps, 720P/240fps video and 20MP image, you can capture high-quality full HD footages.",
    "VOICE CONTROL: You can control your AKASO V50 Elite action camera hands free with voice commands Like “Action Start Video” and “Action Photo”.",
    "SUPERB IMAGE STABLIZATION: Built-in Advanced Electronic Image Stabilization (EIS), your V50 Elite action camera predicts your movements and corrects for camera shake to deliver insanely smooth footage.",
    "OPTIONAL VIEW ANGLE: You can adjust the view angle of this action camera according to your needs between Wide, Medium and Narrow. This sports camera also has the distortion calibration feature, which offers image distortion improvements.",
    "WATERPROOF CAMERA UP TO 131FT: Equipped the improved waterproof case, this underwater camera can deep dive up to 131 feet, ready to capture all details of your adventures. Ideal for water sports such as swimming, surfing, diving, snorkeling, etc."
  ],
  "buybox_winner": {
    "is_prime": false,
    "availability": "in_stock",
    "fulfillment": {
      "type": "2p",
      "is_sold_by_amazon": false,
      "is_fulfilled_by_amazon": true,
      "is_fulfilled_by_third_party": false,
      "is_sold_by_third_party": true,
      "third_party_seller": {
        "name": "AKASO OUTDOOR",
        "link": "https://www.amazon.com/gp/help/seller/at-a-glance.html/ref=dp_merchant_link?ie=UTF8&seller=A2SITDWYE2UYD&isAmazonFulfilled=1"
      }
    },
    "price": {
      "symbol": "$",
      "value": 139.99,
      "currency": "USD",
      "raw": "$139.99"
    }
  },
  "specifications": [
    {
      "name": "Brand Name",
      "value": "AKASO"
    },
    {
      "name": "Item Weight",
      "value": "1.2 pounds"
    },
    {
      "name": "Product Dimensions",
      "value": "2.4 x 1.6 x 1.2 inches"
    },
    {
      "name": "Item model number",
      "value": "V50 Elite"
    },
    {
      "name": "Batteries",
      "value": "2 Lithium Polymer batteries required."
    },
    {
      "name": "Special Features",
      "value": "image-stabilization, zoom"
    },
    {
      "name": "ASIN",
      "value": "B07J4TNYV8"
    },
    {
      "name": "Customer Reviews",
      "value": "4.4 out of 5 stars 992 ratings 4.4 out of 5 stars"
    },
    {
      "name": "Best Sellers Rank",
      "value": "#2,231 in Electronics"
    },
    {
      "name": "Shipping Weight",
      "value": "1.2 pounds"
    },
    {
      "name": "Date First Available",
      "value": "October 17, 2018"
    }
  ],
  "services": [
    {
      "title": "Include installation",
      "price": {
        "symbol": "$",
        "value": 59.29,
        "currency": "USD",
        "raw": "$59.29"
      },
      "whats_included": [
        "Setting up customer-supplied wireless printer",
        "Installing printer device software",
        "Connecting printer to up to 3 devices on network",
        "Testing and verifying proper printer functioning",
        "If additional works are required, additional costs may be incurred"
      ]
    }
  ],
  "attributes": [
    {
      "name": "Size",
      "value": "128 GB"
    },
    {
      "name": "Style",
      "value": "Card and Adapter Only"
    }
  ]
}
```

### TODO
- amazon\_domain param
- 

