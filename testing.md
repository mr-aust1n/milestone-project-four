


# Manual Testing: Item Detail View

This section outlines the manual testing performed for the **Item Detail View** feature of the ReLuvd application.

## ✅ Test Cases


| Test Case                | Expected Result                                                                     | Status   |
|-------------------------|--------------------------------------------------------------------------------------|----------|
| Visit item detail URL   | Go to `/1/` or any valid item ID – item detail page loads with correct info         | ✅ Pass  |
| Click item on homepage  | Click item title or image – redirects to correct item detail page                   | ✅ Pass  |
| Test invalid ID         | Visit `/99999/` or a non-existent ID – returns a 404 page                           | ✅ Pass  |
| Confirm correct item    | Match displayed title, price, description, and image – all content matches database | ✅ Pass  |


![invalid ID](doc_images/invalidID.png) 
![Correct Item ID](doc_images/correctID.png) 