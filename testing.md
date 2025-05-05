


# Manual Testing: Item Detail View

This section outlines the manual testing performed for the **Item Detail View** feature of the ReLuvd application.

## ✅ Test Cases


| Test Case                  | Expected Result                                                                          | Status  |---------------------|--------------------------------------------------------------------------------------------------|---------|
| Visit item detail URL      | Go to `/1/` or any valid item ID - item detail page loads with correct info              | ✅ Pass |
| Click item on homepage     | Click item title or image from homepage - Redirects to correct item detail page          | ✅ Pass |
| Test invalid ID            | Visit `/99999/` or a non-existent ID | Returns a 404 page                                | ✅ Pass |
| Confirm correct item       | Match displayed title, price, description, image - All content matches item data entered | ✅ Pass |

![invalid ID](doc_images/invalidID.png) 
![invalid ID](doc_images/correctItem.png) 