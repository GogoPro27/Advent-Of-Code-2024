

def main():
    k = int(input())
    capybara_scores = list(map(int, input().split(",")))
    capybara_scores = sorted(capybara_scores)

    max_count = 0

    for i in range(len(capybara_scores)):
        current_score = capybara_scores[i]
        limit = current_score+k
        count = 1

        for j in range(i+1,len(capybara_scores)):
            next_score = capybara_scores[j]
            if next_score <= limit:
                count+=1
            else:
                break
        if count>max_count:
            max_count = count

    print(max_count)

if __name__ == '__main__':
    main()