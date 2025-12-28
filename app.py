# تابع دریافت ورودی از کاربر
# ورودی باید شامل حروف باشد و چند کلمه‌ای قابل قبول است
def get_user_input():
    while True:
        # گرفتن ورودی از کاربر
        user_input = input("please Enter : \n")
        # بررسی اینکه هر کلمه فقط شامل حروف باشد
        if all(word.isalpha() for word in user_input.split()):
            # اگر ورودی معتبر بود رشته رو باز میگردونه
            return user_input
        # در غیر این صورت ارور میده
        else:
            print("Please Input Vaild Word : \n")
# تابع بررسی طولانی‌ترین کلمات
def check_tekrar(user_input):
    # تعریف متغیر words و حذف فاصله و جداسازی کلمات از جمله و تبدیل آن به لیست
    words = user_input.strip().split()
    #محاسبه طول هر کلمه جدا شده موجود در لیست
    length = [len(word) for word in words]
    max_length = max(length)
    longest_words = " ".join(filter(lambda w : len(w) == max_length , words))
    # چاپ هر کلمه طولانی همراه با طول آن
    for w in longest_words.split():
        print(f"{w} ({max_length} letters)")

# بلوک اصلی برنامه
if __name__ == "__main__":
    # گرفتن ورودی از کاربر
    user_input = get_user_input()
    # پیدا کردن و چاپ طولانی‌ترین کلمات
    check_tekrar(user_input)