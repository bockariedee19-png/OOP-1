
# Crop Yield Monitoring System

# Step 1: Create the CropRecord class
class CropRecord:
    def __init__(self, crop_name, area, harvest):
        self.crop_name = crop_name
        self.area = area
        self.harvest = harvest

    # Step 2: Calculate yield per hectare
    def calculate_yield(self):
        if self.area <= 0:
            return 0
        return self.harvest / self.area


# Step 3: Create a list for storing crop records
crops = []


# Step 4: Create a function to add crop records
def add_crop():
    crop_name = input("Enter crop name: ")
    area = float(input("Enter farm area in hectares: "))
    harvest = float(input("Enter harvest in kg: "))

    crop = CropRecord(crop_name, area, harvest)
    crops.append(crop)

    print("Crop record added successfully!")


# Step 5: Create a function to display crop records
def display_crops():
    print("\n=== CROP RECORDS ===")

    if len(crops) == 0:
        print("No crop records available.")
        return

    for crop in crops:
        print("\nCrop Name:", crop.crop_name)
        print("Farm Area:", crop.area, "hectares")
        print("Harvest:", crop.harvest, "kg")
        print("Yield per Hectare:",
              crop.calculate_yield(), "kg")


# Step 6: Run the program
while True:
    print("\n=== CROP YIELD MONITORING SYSTEM ===")
    print("1. Add Crop Record")
    print("2. Display Crop Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_crop()
    elif choice == "2":
        display_crops()
    elif choice == "3":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please try again.")