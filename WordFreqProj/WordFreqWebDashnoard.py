from mylib import myTextAnalyzer as ta

# 데이터 로딩
data_filename = '.\data\daum_movie_review.csv'
column = 'review'
corpus = ta.load_corpus_from_csv(data_filename, column)
# print(corpus[:5])

# 토큰화 -> 빈도수 추출
from konlpy.tag import Okt
tokenizer = Okt().pos
my_tags = ['Noun', 'Verb', 'Adjective']
my_stopwords = ['영화', '정말', '진짜', '보고', '연기','생각','것','배우','사람','스토리','더','잘','하는','눈물','점','좀','마지막','그','시간'
                ,'입니다','마동석','그냥','정도','광주','윤계상','기대','내용','돈','할','볼','꼭','장면','있는','원작','내','말','본','왜'
                ,'수', '평점', '이', '가', '은', '는', '의', '에', '있다','...','..','ㅡㅡ','....']
tokens = ta.tokenize_korean_corpus(corpus, tokenizer, my_tags, my_stopwords)
# print(tokens[:10])

counter = ta.analyze_word_freq(tokens)
# print(list(counter.items())[:10])

# 시각화
# 1. 수평 막대그래프
num_words = 20
title = '영화 리뷰'
ylabel = '키워드'
xlabel = '빈도수'
font_path = "c:/Windows/Fonts/malgun.ttf"
ta.visualize_barhgraph(counter, num_words, title, xlabel, ylabel, font_path)

# 2. 워드클라우드
ta.visualize_wordcloud(counter, num_words, font_path)