def pts_to_grade(points):
    if points >= 18:
        return 'Excellent'
    elif points >= 14:
        return 'Good'
    elif points >= 10:
        return 'Satisfactory'
    else:
        return 'Fail'

# Testowanie funkcji
test_result = 15
<<<<<<< HEAD
print(f'Z wynikiem {test_result} Twoja ocena to: {pts_to_grade(test_result)}')
=======
print(f'Z wynikiem {test_result} Twoja ocena to: {pts_to_grade(test_result)}')
>>>>>>> b4770c5f2e0d0ca7ff2ce14518d1262a0494f257
