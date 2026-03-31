def solution(num_list):
    t=1
    p=0
    for i in num_list:
        t*=i
        p+=i
    if t<p**2:
        return 1
    else:return 0
  