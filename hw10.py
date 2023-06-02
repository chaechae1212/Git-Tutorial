import pickle

def input_scores():
    scores = []
    while True:
        score = int(input("#{}? ".format(len(scores)+1)))
        if score < 0:
            break
        scores.append(score)
    return scores

def get_average(scores):
    return round(sum(scores) / len(scores), 1)

def show_scores(scores):
    print("개인점수:", end=" ")
    for score in scores:
        print(score, end=" ")
    print()

def save_scores(scores, filename):
    with open(filename, "wb") as file:
        pickle.dump(scores, file)

def load_scores(filename):
    with open(filename, "rb") as file:
        scores = pickle.load(file)
    return scores

def main():
    filename = "score.bin"
    try:
        scores = load_scores(filename)
        print("[파일읽기]")
        show_scores(scores)
        average = get_average(scores)
        print("평균:", average)
    except FileNotFoundError:
        print("[파일 없음]")

    print("[점수 입력]")
    scores = input_scores()
    show_scores(scores)
    average = get_average(scores)
    print("평균:", average)

    save_scores(scores, filename)
    print("[파일 저장]")

main()
