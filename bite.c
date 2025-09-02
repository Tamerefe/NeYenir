#include <stdio.h>

int main()
{

    int foddie;

    printf("1.) Doner \n2.) Chicken Wing \n3.) Hamburger \n4.) Pizza \n5.) Pasta \n6.) Meatball");
    printf("\nPlease enter a number: ");
    scanf("%d", &foddie);
    printf("\nYou can eat these with; ");

    switch (foddie)
    {
    case 1:
        printf("\n- Lentil Soup \n- Chips \n- Bread \n- Salad \n- Pickled Hot Pepper \n- Ayran \n- Walnut Wire Kadayif");
        break;
    case 2:
        printf("\n- Pasta with Pesto Sauce \n- Chips \n- Coleslaw \n- Rice \n- Onion Rings \n- Ayran \n- Salad");
        break;
    case 3:
        printf("\n- Tomato Soup \n- Carrot Tarator \n- Yogurt \n- Strawberry Lemonade \n- Gherkin Pickle \n- Onion Rings \n- Baklava");
        break;
    case 4:
        printf("\n- Cajun Spiced French Fries \n- Chips \n- Crispy Chicken \n- Cheddar Croquette \n- Pickled Hot Pepper \n- Cool Lime \n- Onion Rings");
        break;
    case 5:
        printf("\n- Lentil Soup \n- Tomato Soup \n- Turkey Meatballs \n- Potato Meatball \n- Magnolia Dessert \n- Mushrooms with Cheddar Cheese \n- Chicken with Curry Sauce");
        break;
    case 6:
        printf("\n- Lentil Soup \n- Chips \n- Bread \n- Rice \n- Mac and Cheese \n- Potato Balls \n- Zucchini Pancakes");
        break;
    default:
        break;
    }

    return 0;
}