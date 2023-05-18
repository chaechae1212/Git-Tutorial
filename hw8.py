def shopping_bag_simulation():
    shopping_bag = {}

    while True:
        action = input("[구입] 또는 [검색]을 입력하세요: ")

        if action == "구입":
            item = input("상품명을 입력하세요: ")

            if item == "":
                break

            quantity = int(input("수량은? "))
            shopping_bag[item] = quantity
            print(f"장바구니에 {item} {quantity}개가 담겼습니다.")

        elif action == "검색":
            item = input("장바구니에서 확인하고자 하는 상품은? ")

            if item in shopping_bag:
                print(f"{item}은(는) {shopping_bag[item]}개 담겨 있습니다.")
            else:
                print(f"장바구니에 {item}은(는) 없습니다.")

        else:
            print("유효한 동작을 입력하세요.")

    print("장바구니 보기:", shopping_bag)


shopping_bag_simulation()
