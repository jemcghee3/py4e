def computegrade(decimal_score):
    # check input for validity
    try:
        decimal_score = float(decimal_score)
    except:
        return 'Bad score'
    if decimal_score > 1 or decimal_score < 0:
        return 'Bad score'
    # evaluate the scores to grades
    elif decimal_score >= 0.9:
        return 'A'
    elif decimal_score >= 0.8:
        return 'B'
    elif decimal_score >= 0.7:
        return 'C'
    elif decimal_score >= 0.6:
        return 'C'
    else:
        return 'F'

score = input('Enter score: ')
grade = computegrade(score)
print(computegrade(score))
