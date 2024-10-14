from webStore import app, db, Album

albums = [
    {
        "name": "6 feet beneath the moon",
        "Artist": "King Krule",
        "price": 15.99, 
        "description": """Six Feet Beneath the Moon is the debut album 
        by King Krule, the musical alias of English singer-songwriter 
        Archy Marshall. Released in 2013, the album merges elements 
        of punk, jazz, and trip-hop, creating a moody and introspective 
        atmosphere. Marshall's distinctive deep voice narrates tales of 
        urban ennui, alienation, and personal struggles, accompanied by raw 
        and gritty instrumentals. With its haunting melodies and poetic lyricism, 
        'Six Feet Beneath the Moon' solidified King Krule as a unique voice in 
        contemporary music, showcasing his ability to craft evocative and 
        atmospheric soundscapes.""", 
        "img": "six_feet_beneath_the_moon.jpg", 
        "Enviroments": 0.2
     },
    {
        "name": "Forca Bruta",
        "Artist": "Jorge Ben Jor",
        "price": 17.99, 
        "description": """"Jorge Ben's Força Bruta" is a seminal album in Brazilian 
        music history, released in 1970. Led by the iconic Brazilian singer-songwriter 
        Jorge Ben, the album is a fusion of samba, funk, and rock, infused with Afro-Brazilian 
        rhythms and infectious melodies. "Força Bruta" showcases Ben's charismatic vocals, 
        inventive guitar playing, and clever songwriting, addressing themes of social issues, 
        love, and cultural identity. The album's title track, "Força Bruta," became an anthem 
        of empowerment and resilience, while other tracks like "Pulo, Pulo" and "Que Maravilha" 
        exemplify Ben's innovative blend of genres. With its vibrant energy and enduring appeal, 
        "Força Bruta" remains a cornerstone of Brazilian popular music, influencing generations 
        of musicians worldwide.""", 
        "img": "Forca_Bruta.jpg", 
        "Enviroments": 0.8
     },
    {
        "name": "Frank",
        "Artist": "Amy Winehouse",
        "price": 18.99, 
        "description": """'Amy Winehouse's 'Frank'' is the debut studio album by the British 
        singer-songwriter, released in 2003. The album showcases Winehouse's distinctive blend 
        of jazz, soul, and R&B, fused with her honest and introspective lyricism. Named after
        Frank Sinatra, one of Winehouse's influences, the album features tracks that explore 
        themes of love, heartbreak, and personal experiences with a raw and unfiltered authenticity. 
        Winehouse's soulful vocals, accompanied by jazzy instrumentation, create a captivating 
        and emotive listening experience. Tracks like "Stronger Than Me" and "Take the Box" 
        highlight Winehouse's vocal prowess and lyrical depth, while "F**k Me Pumps" and 
        "In My Bed" reveal her sharp wit and candid storytelling. "Frank" introduced Winehouse 
        as a formidable talent in the music industry, setting the stage for her later 
        critically acclaimed album, "Back to Black.""",
        "img": "Frank.jpg", 
        "Enviroments": 1.3
     },
    {
        "name": "Inner City Life",
        "Artist": "Goldie",
        "price": 19.99, 
        "description": """'Inner City Life' is a seminal track by British electronic music 
        producer and DJ Goldie, released in 1994 as part of his album "Timeless." 
        The song is a groundbreaking fusion of drum and bass, jungle, and ambient music, 
        featuring ethereal vocals by Diane Charlemagne. "Inner City Life" captures the essence 
        of urban existence, with its pulsating beats, haunting melodies, and poignant lyrics 
        reflecting the struggles and experiences of city dwellers. The track's innovative 
        production techniques, intricate rhythms, and emotive atmosphere helped propel it to 
        iconic status within the electronic music genre. "Inner City Life" remains a timeless 
        classic and a testament to Goldie's influence on the evolution of electronic music.""", 
        "img": "Inner_city_life.jpg", 
        "Enviroments": 6.3  
     },
    {
        "name": "Jorge Ben",
        "Artist": "Jorge Ben Jor",
        "price": 12.99, 
        "description": """Jorge Ben's self-titled album, commonly referred to as "Jorge Ben" or 
        "Jorge Ben (1969)," is a landmark release in Brazilian music history. Released in 1969, 
        this influential album marks a pivotal moment in Ben's career, showcasing his evolution 
        as a songwriter and performer. With its fusion of samba, bossa nova, funk, and rock, 
        the album represents a departure from traditional Brazilian music, introducing 
        innovative arrangements and rhythms. Tracks like "Que Pena" and "Pais Tropical" 
        exemplify Ben's signature style, featuring infectious grooves, catchy melodies, 
        and socially conscious lyrics. "Jorge Ben (1969)" solidified Ben's status as one of 
        Brazil's most important musical figures and remains a timeless classic beloved by fans 
        around the world.""", 
        "img": "Jorge_Ben.jpg", 
        "Enviroments": 0.2
    },
    {
        "name": "Let My People Go",
        "Artist": "Dorando",
        "price": 11.99, 
        "description": """"Dorando's 'Let My People Go'" is a rare soul gem, released in 1971 by
        American soul singer Dorando Pulliam. The song features a powerful vocal performance by 
        Dorando, backed by a lush arrangement of horns, strings, and a groovy rhythm section. 
        With its gospel-infused lyrics and soulful delivery, "Let My People Go" is both a heartfelt 
        plea for freedom and a stirring call to action. The song's infectious groove and emotional 
        depth have made it a sought-after classic among collectors of rare soul records. Dorando's 
        impassioned performance and the song's timeless message continue to resonate with listeners 
        to this day.""", 
        "img": "Let_My_People_Go.jpg", 
        "Enviroments": 0.5
    }
]

with app.app_context():
    db.create_all()
    for album in albums:
        newAlbum = Album(name=album["name"], artist=album["Artist"], price=album["price"], description=album["description"], image=album["img"], environment=album["Enviroments"])
        db.session.add(newAlbum)
    
    db.session.commit()