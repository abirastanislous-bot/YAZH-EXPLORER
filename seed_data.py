import sqlite3

def seed_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Clear existing data (so we don't get duplicates)
    cursor.execute("DELETE FROM places")
    
    places_data = [
        # 1. St. Anthony's Church, Passaiyoor
        ("St. Anthony's Church, Passaiyoor", "Religious",
         "A historic Catholic church in the heart of Passaiyoor, just 3km south of Jaffna city. Built in the 19th century, this landmark is famous for its annual feast and beautiful colonial architecture. It serves as a spiritual center for the local Catholic community and welcomes visitors of all faiths.",
         "6:00 AM - 6:00 PM", "Free", 0.1,
         "Dress modestly. Visit during the annual feast in June for a special experience. Photography allowed outside.",
         "Built in the 19th century, this church has been a landmark of Passaiyoor for generations. It survived the civil war and remains a symbol of faith and resilience for the local community.",
         "021-222-XXXX", 9.6615, 80.0255, "st_anthonys"),
        
        # 2. Nallur Kandaswamy Temple
        ("Nallur Kandaswamy Temple", "Religious",
         "One of the most prominent Hindu temples in Sri Lanka, dedicated to Lord Murugan. Known for its golden gopuram (tower) and vibrant annual festival in August, this temple has been a spiritual center for over a thousand years.",
         "5:00 AM - 8:00 PM", "Free", 3.0,
         "Remove footwear before entering. Dress conservatively (cover shoulders and knees). The annual festival in August is spectacular but very crowded.",
         "Originally built in 948 AD, the temple was destroyed by the Portuguese in 1620 and rebuilt in its current form in the 18th century. It is one of the most important Hindu pilgrimage sites in Sri Lanka.",
         "021-222-XXXX", 9.6833, 80.0333, "nallur_temple"),
        
        # 3. Jaffna Fort
        ("Jaffna Fort", "Heritage",
         "A massive Portuguese-built fort dating back to 1618, later expanded by the Dutch. It stands as a symbol of Jaffna's colonial history and offers stunning views of the Jaffna lagoon. A must-visit for history enthusiasts.",
         "8:00 AM - 6:00 PM", "Free", 3.0,
         "Best visited in the early morning or late evening. Wear comfortable shoes. Bring water and a hat.",
         "Built by the Portuguese in 1618, it was captured by the Dutch in 1658 who expanded it significantly. The fort played a key role in Sri Lanka's colonial history and was later used by the British.",
         "011-XXXXXXX", 9.6615, 80.0089, "jaffna_fort"),
        
        # 4. St. Mary's Cathedral
        ("St. Mary's Cathedral", "Religious",
         "The seat of the Roman Catholic Diocese of Jaffna, this cathedral is known for its peaceful atmosphere and beautiful stained-glass windows. Located just 1.5km from Passaiyoor.",
         "6:00 AM - 7:00 PM", "Free", 1.5,
         "Visit during the morning mass for a peaceful experience. Dress modestly. Photography allowed inside.",
         "Consecrated in 1794, this cathedral has served the Catholic community of Jaffna for over two centuries. It features beautiful European-style architecture blended with local design.",
         "021-222-XXXX", 9.6750, 80.0180, "st_marys"),
        
        # 5. Jaffna Public Library
        ("Jaffna Public Library", "Cultural",
         "An iconic cultural symbol of Jaffna, this library was rebuilt after being destroyed in 1981. It stands as a testament to the region's love for knowledge and resilience.",
         "9:00 AM - 6:00 PM", "Free", 2.5,
         "Best visited in the morning. The architecture is stunning, especially the white pillars and golden dome.",
         "Established in 1933, it was one of the largest libraries in Asia with over 97,000 books. It was destroyed by fire in 1981 and fully rebuilt by 2003. It symbolizes the cultural revival of Jaffna.",
         "021-222-XXXX", 9.6645, 80.0116, "library"),
        
        # 6. Casuarina Beach
        ("Casuarina Beach", "Nature",
         "A pristine stretch of golden sand lined with casuarina trees, located 20km from Passaiyoor. The calm waters make it perfect for relaxation and family picnics.",
         "Open 24 hours", "Free", 20.0,
         "Bring sunscreen, water, and a hat. Best time to visit is early morning or sunset. Very peaceful on weekdays.",
         "A naturally beautiful beach famous for its casuarina trees. It was a popular local picnic spot for decades and is now becoming a tourist destination.",
         "N/A", 9.8250, 80.2450, "casuarina"),
        
        # 7. Kadurugoda Temple
        ("Kadurugoda Temple", "Religious",
         "An ancient Buddhist temple with historical stupas dating back over 2,000 years. Located 20km from Passaiyoor, it is an important archaeological site.",
         "6:00 AM - 6:00 PM", "Free", 20.0,
         "Respectful behavior required. Remove footwear before entering the temple grounds. Ask before taking photos of monks.",
         "Excavations have revealed over 60 stupas and ruins dating back to the Anuradhapura period. It is one of the few Buddhist sites in the predominantly Hindu Jaffna region.",
         "N/A", 9.7850, 80.1350, "kadurugoda"),
        
        # 8. Manalkadu Beach
        ("Manalkadu Beach", "Nature",
         "A unique beach known for its sand dunes and the ruins of an old Dutch church. Located 18km from Passaiyoor, it offers a peaceful escape from the city.",
         "Open 24 hours", "Free", 18.0,
         "Bring water and snacks. The sand dunes are best explored in the early morning. Watch out for strong sun.",
         "The name 'Manalkadu' means 'sandy forest'. The Dutch church ruins date back to the 17th century. The dramatic landscape has been featured in several Sri Lankan films.",
         "N/A", 9.8030, 80.2250, "manalkadu"),
        
        # 9. Sangiliyan Thoppu
        ("Sangiliyan Thoppu", "Heritage",
         "A historical site associated with the Jaffna Kingdom, located just 3km away. It is believed to be the site where King Sankiliyan ruled.",
         "8:00 AM - 6:00 PM", "Free", 3.0,
         "Best visited in the morning. Read about King Sankiliyan before visiting to appreciate the history.",
         "Named after King Sankiliyan II, the last king of the Jaffna Kingdom (reigned 1617-1619). The site includes ruins of a royal archway and is associated with the Portuguese conquest of Jaffna.",
         "N/A", 9.6700, 80.0200, "sangiliyan"),
        
        # 10. Durayappah Stadium
        ("Durayappah Stadium", "Cultural",
         "A historic sports venue in Jaffna city, known for hosting cricket and athletic events. A cultural hub for the local community.",
         "8:00 AM - 6:00 PM", "Free", 3.0,
         "Check for scheduled matches. Great for cricket fans. The atmosphere during local matches is vibrant.",
         "Named after a former mayor of Jaffna, this stadium has hosted many important sporting events and is a symbol of Jaffna's sporting spirit.",
         "N/A", 9.6650, 80.0150, "durayappah"),
    ]
    
    cursor.executemany('''
        INSERT INTO places (name, category, description, opening_hours, entrance_fee, distance, travel_tips, historical_background, contact_details, latitude, longitude, image_folder)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', places_data)
    
    conn.commit()
    conn.close()
    print("✅ Database seeded with 10 places successfully!")

if __name__ == '__main__':
    seed_data()
