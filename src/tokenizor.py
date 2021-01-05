import pyonmttok
from opennmt.config import load_config
from MicroTokenizer.tokenizer import Tokenizer as MicroTokenizer


class Tokenizer(object):
    def __init__(self, config):
        tokenizer_config = load_config(config)
        self.tokenizer = pyonmttok.Tokenizer(**tokenizer_config)
        self.chinese_tokenizer = MicroTokenizer()

    def process(self, texts):
        # TODO: why texts, should be one text here?
        all_tokens = []
        lengths = []
        max_length = 0

        for text in texts:
            token_str = " ".join(
                self.chinese_tokenizer.cut_by_DAG(text.replace("\n", ""))
            )
            tokens, _ = self.tokenizer.tokenize(token_str)
            length = len(tokens)

            print(tokens)
            print(length)

            all_tokens.append(tokens)
            lengths.append(length)
            max_length = max(max_length, length)

        for tokens, length in zip(all_tokens, lengths):
            if length < max_length:
                tokens += [""] * (max_length - length)

        print(all_tokens)

        inputs = {
            "tokens": tf.constant(all_tokens, dtype=tf.string),
            "length": tf.constant(lengths, dtype=tf.int32),
        }

        print(inputs)
        return inputs

    def postprocess(self, outputs):
        texts = []
        for tokens, length in zip(outputs["tokens"].numpy(), outputs["length"].numpy()):
            tokens = tokens[0][: length[0]].tolist()
            texts.append(self.tokenizer.detokenize(tokens))
        return "".join(texts)
