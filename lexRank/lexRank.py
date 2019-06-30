import sumy.summarizers.lex_rank as lex_rank_module
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.utils import get_stop_words

def getTitle(text):

	parser = PlaintextParser.from_string(text, Tokenizer('japanese'))
	summarizer = LexRankSummarizer()
	summarizer.stop_words = [' ']  # スペースをストップワードにすることで除外する
	
	sentence = summarizer(parser.document, 1)
	
	title = ''
	if not sentence:
		title = ""
	else:
		title = str(sentence[0]).replace('。', '')
	return title