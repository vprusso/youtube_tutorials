---
title: "System Design: Photo Sharing Application"
---

# Goals

- Design a photo sharing web application. Similar to Instagram, Flickr, etc.
. . .

- Step through the high-level requirements for such an application.
. . .

- Cover techniques for building and scaling this service.

# Attributions

- Content based on: 
[Designing Instagram by Educative](https://www.educative.io/collection/page/5668639101419520/5649050225344512/5673385510043648)

# Basic Functionality Requirements

- Upload and download photos from service.
. . .

- Search for photos based on titles.
. . .

- Allow users to follow other users.
. . .

- Be able to display the feed of user as homepage.

# Basic Service Requirements

- Low latency for news feed generation.
. . .

- Reliably store photos.
. . .

- Allow users to upload as many photos as they wish.

# Not Required
- Other requirements could be asked by the interviewer, but for our
  application we will side-step these particularl attributes.
. . .

    1. Commenting on photos. 

    2. Tagging photos.

    3. Face recognition and user tagging.

    4. Suggesting who to follow.

# Capacity Estimation

- Capacity figures obtained from: Educative.
. . .

    1. 500 million total users. 1 million active users daily.
. . . 

    2. 2 million photos each day with roughly ~23 photos uploaded each second.
. . .

    3. Average photo size will be around ~200KB:
        2 million * 200 KB = 400 GB
. . .
        
    4. Total space required (assuming we store photos for 10 years):
        400 GB * 365 (days) * 10 (years) ~= 1425 TB

# High-level Requirements

- Users should be able to:

    1. Upload image.
. . .

    2. Search for image.
. . .


- This will involve some storage solution for:

    1. Storing the images that are uploaded.
. . .

    2. Storing metadata about the images (caption, location, etc.)

# Database Design

- 


# Test

-

# Further Resources 

- Content based on: 
[Designing Instagram by Educative](https://www.educative.io/collection/page/5668639101419520/5649050225344512/5673385510043648)
