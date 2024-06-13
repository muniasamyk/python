def library_book(book_available, borrowing_duration, daily_late_fee):
    if book_available == True:
        if borrowing_duration > 0:
            message = "book can be borrowed"
            success = True
            if borrowing_duration <= 5:
                late_fee = 0.0
            else:
                additional_day = borrowing_duration-5
                late_fee = additional_day * daily_late_fee
                print(late_fee)
        else:
            late_fee = 0.0
            message = "book not available"
            success = False
    else:
        late_fee = 0.0
        message = "book is not available for borrow"
        success = False
    return{
        "success": success,
        "message": message,
        "late_fee": late_fee
    }
result = library_book(True, 5, 50.0)
print(result)