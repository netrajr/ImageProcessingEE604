# EE604: Image Processing Assignment

This repository contains the solutions for the assignments given in the EE604 course. Each problem tackles a real-world challenge using image processing and audio analysis techniques. The objective and approach for each question are detailed below.

## Assignment 1

### 1. Jai Hind

**Objective:**
To generate a reference image of the Indian flag seen by a drone from a non-optimal position, allowing it to adjust its position with minimal movement until the correct reference image is observed.

**Approach:**
- Process the input image to identify and adjust for variations in tilt and height seen by the drone.
- Output a standardized reference image of size 600x600 pixels with specific circle and spoke dimensions.
- Consider edge cases where input images might vary in size and alignment.

### 2. Eent Ka Jawab Image Se

**Objective:**
To classify the quality of bricks based on the sound they produce when struck together, determining whether they are of high (metal-like) or low (cardboard-like) quality.

**Approach:**
- Convert audio inputs of brick sounds to spectrograms using windowed Fourier transforms.
- Analyze the spectrograms to classify the bricks as either "metal" or "cardboard" based on their acoustic properties.
- Ensure the program is robust enough to handle multiple test cases with varying audio quality.

### 3. Anuprasth Drishyam

**Objective:**
To realign scanned images of ancient Sanskrit texts so that the text appears horizontally aligned for proper optical character recognition (OCR).

**Approach:**
- Process the input images to detect and correct any misalignment.
- Ensure that the output image has all text characters fully visible and aligned horizontally.
- The output image size can differ from the input, focusing on achieving perfect alignment.

## Assignment 2

### 1. The Lava

**Objective:**
To detect and mask the lava region in images captured after a volcanic eruption, aiding in accurate lava flow estimation.

**Approach:**
- Analyze input images to identify and isolate the lava region, generating a binary mask with the lava region marked in white and the non-lava region in black.
- Ensure the mask accurately represents the lava flow for emergency response and environmental impact assessments.
- Use the Dice coefficient overlap for evaluating the accuracy of the detection.

### 2. Pro-night with or without Camera Flash?

**Objective:**
To fuse images taken with and without flash to produce a final image that preserves the scene's natural ambiance while removing unwanted artifacts caused by flash photography.

**Approach:**
- Implement a cross bilateral filter to combine flash and no-flash images.
- The fused output should enhance the overall quality, retaining necessary details while eliminating flash-induced artifacts.
- Prioritize computational speed without compromising the output quality.

### 3. The Victory Over Delusion

**Objective:**
To determine whether the image of Ravana presents a real or manipulated view, identifying if the confrontation is genuine or a delusion.

**Approach:**
- Analyze the given input image to distinguish between real and fake representations of Ravana.
- The program outputs either "real" or "fake" based on the detection of any manipulated heads.
- Handle various input scenarios, including those with deceptive visual cues.
