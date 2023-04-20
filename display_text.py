import cv2
import numpy as np

# Create a blank image (white background)
image = np.ones((800, 1000, 3), dtype=np.uint8) * 255

# Define text properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
font_thickness = 1
color = (0, 0, 0)

# Define text data
text_data = '''Broad Options\tYear 0\tYear 1\tYear 2\tYear 3
Diamond/Engagement Ring Sales
Units Sold\t80\t100\t115\t125

Revenue
Diamond Sales\t267,800\t334,799.93\t384,904.72\t418,513.91
Engagement Ring Sales\t64,350\t80,388.07\t92,561.28\t100,471.09

Total Revenue\t332,150\t415,188\t477,466\t518,985

Expenses
Cost Of Diamonds\t221,431\t227,874\t234,710\t241,712
Cost Of Rings\t28,794\t29,658\t30,547\t31,464
Rent\t6,480\t6,674\t6,875\t7,082
Advertising\t9,775\t10,064\t10,366\t10,677
Misc/Traveling\t1,350\t1,391\t1,433\t1,476
Utilities\t449\t462\t476\t490
Payroll\t11,440\t11,783\t12,136\t12,500
Total Expenses\t291,356\t286,906\t295,543\t304,401

Profit/Losses\t40,794\t128,282\t181,923\t214,584'''

# Split text data into lines
lines = text_data.split('\n')

# Define the initial position for the text
position = (20, 30)

# Iterate through the lines and add them to the image
for line in lines:
    # Split each line into columns
    columns = line.split('\t')
    
    # Iterate through the columns and add them to the image
    x_offset = 0
    for column in columns:
        size = cv2.getTextSize(column, font, font_scale, font_thickness)[0]
        position_with_offset = (position[0] + x_offset, position[1])
        cv2.putText(image, column, position_with_offset, font, font_scale, color, font_thickness)
        x_offset += size[0] + 10

    position = (position[0], position[1] + 30)

# Display the image
cv2.imshow('Text Box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image
cv2.imwrite('output.png', image)
