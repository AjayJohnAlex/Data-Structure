from collections import OrderedDict
import numpy as np
import math


class TextRank4Keyword():
    """Extract keywords from text"""

    def __init__(self):
        self.d = 0.85  # damping coefficient, usually is .85
        self.min_diff = 1e-5  # convergence threshold
        self.steps = 10  # iteration steps
        self.node_weight = None  # save keywords and its weight

    def get_vocab(self, sentences_data):
        """Get all tokens"""
        vocab = OrderedDict()
        i = 0
        for sentence in sentences_data:
            for word in sentence:
                if word not in vocab:
                    vocab[word] = i
                    i += 1
        # print('VOCAB', vocab, '\n', 'VOCAB len', len(vocab), '\n')
        return vocab

    def get_token_pairs(self, window_size, sentences_data):
        """Build token_pairs from windows in sentences"""
        token_pairs = list()
        for sentence in sentences_data:
            for i, word in enumerate(sentence):
                for j in range(i + 1, i + window_size):
                    if j >= len(sentence):
                        break
                    pair = (word, sentence[j])
                    if pair not in token_pairs:
                        token_pairs.append(pair)
        # print('token_pairs',  '\n', token_pairs, '\n',
              # 'token_pairs len ',  '\n', len(token_pairs), '\n')

        return token_pairs

    def symmetrize(self, a):
        # print('symmetrize', '\n', a + a.T - np.diag(a.diagonal()), '\n')
        # print(a == (a + a.T - np.diag(a.diagonal())))
        print('a: \n', a)
        print('a.T: \n', a.T)
        print('a.diagonal: \n', a.diagonal())
        print('np.diag(a.diagonal()): \n', np.diag(a.diagonal()))
        W = np.maximum(a, a.T)
        print('W: \n', W)
        print('symmetrize', '\n', a + a.T - np.diag(a.diagonal()), '\n')

        return a + a.T - np.diag(a.diagonal())

    def get_matrix(self, vocab, token_pairs):
        """Get normalized matrix"""
        # Build matrix
        vocab_size = len(vocab)
        g = np.zeros((vocab_size, vocab_size), dtype='float')
        for word1, word2 in token_pairs:
            i, j = vocab[word1], vocab[word2]
            g[i][j] = 1

        # Get Symmeric matrix
        g = self.symmetrize(g)
        print('g:', g, '\n')
        # Normalize matrix by column
        norm = np.sum(g, axis=0)
        # print('vocab.keys()', '\n', vocab.keys())
        # print('norm', '\n', norm)
        # this is ignore the 0 element in norm
        g_norm = np.divide(g, norm, where=norm != 0)
        print('g_norm', '\n', g_norm, '\n')

        return g_norm

    def get_keywords(self, number=10):
        """Print top number keywords"""
        node_weight = OrderedDict(
            sorted(self.node_weight.items(), key=lambda t: t[1], reverse=True))
        for i, (key, value) in enumerate(node_weight.items()):
            print(key + ' - ' + str(value))
            if i > number:
                break

    def analyze(self, sentences_data, candidate_pos=['NOUN', 'PROPN'],
                window_size=4, lower=False, stopwords=list()):
        """Main function to analyze text"""

        # # Set stop words
        # self.set_stopwords(stopwords)

        # # Pare text by spaCy
        # doc = nlp(text)

        # # Filter sentences
        # sentences = self.sentence_segment(
        #     doc, candidate_pos, lower)  # list of list of words

        # Build vocabulary
        vocab = self.get_vocab(sentences_data)

        # Get token_pairs from windows
        token_pairs = self.get_token_pairs(window_size, sentences_data)

        # Get normalized matrix
        g = self.get_matrix(vocab, token_pairs)

        # Initionlization for weight(pagerank value)
        pr = np.array([0.1] * len(vocab))
        # print('pr', '\n', pr, '\n')

        # Iteration
        previous_pr = 0
        for epoch in range(self.steps):
            pr = (1 - self.d) + self.d * np.dot(g, pr)
            if abs(previous_pr - sum(pr)) < self.min_diff:
                break
            else:
                previous_pr = sum(pr)

        # Get weight for each node
        node_weight = dict()
        for word, index in vocab.items():
            node_weight[word] = pr[index]

        self.node_weight = node_weight


sentences_data = [['China', 'Earth', 'described', 'China', 'budget', 'science', 'fiction'], ['time', 'Wandering', 'Earth',
                                                                                             'feels', 'throwback', 'eras', 'filmmaking'], ['film', 'cast', 'setting', 'tone', 'science']]

tr4w = TextRank4Keyword()
tr4w.analyze(sentences_data, candidate_pos=[
             'NOUN', 'PROPN'], window_size=4, lower=False)
tr4w.get_keywords(15)
