import pickle

#profile.pickle 파일을 읽어서 profile_file에 저장 그리고 자동 종료됨-close 필요 없음
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# with open("study.txt", "w" , encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부 중 입니다!")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())