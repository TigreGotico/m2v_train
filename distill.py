
from model2vec.distill import distill

models = [
    "dvilares/bertinho-gl-small-cased",
    "dvilares/bertinho-gl-base-cased",
    #"BSC-LT/mRoBERTa",  # fails
    #"BSC-LT/RoBERTa-ca",  # fails
    "google-bert/bert-base-multilingual-cased",
    "sentence-transformers/LaBSE",
    "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
    "sentence-transformers/distiluse-base-multilingual-cased-v2",
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
]

for m in models:
    m2v_model = distill(model_name=m, pca_dims=256)
    m2v_model.save_pretrained(m + "-distill256")


# TODO - figure out why BSC models are failing
# Some weights of RobertaModel were not initialized from the model checkpoint at BSC-LT/mRoBERTa and are newly initialized: ['pooler.dense.bias', 'pooler.dense.weight']
# You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
# Encoding tokens: 100%|██████████| 255867/255867 [24:14<00:00, 175.90 tokens/s]
# Token <0x00> has no merges.
# Token <0x01> has no merges.
# Token <0x02> has no merges.
# Token <0x03> has no merges.
# Token <0x04> has no merges.
# Token <0x05> has no merges.
# Token <0x06> has no merges.
# Token <0x07> has no merges.
# Token <0x08> has no merges.
# Token <0x09> has no merges.
# Token <0x0A> has no merges.
# Token <0x0B> has no merges.
# Token <0x0C> has no merges.
# Token <0x0D> has no merges.
# Token <0x0E> has no merges.
# Token <0x0F> has no merges.
# Token <0x10> has no merges.
# Token <0x11> has no merges.
# Token <0x12> has no merges.
# Token <0x13> has no merges.
# Token <0x14> has no merges.
# Token <0x15> has no merges.
# Token <0x16> has no merges.
# Token <0x17> has no merges.
# Token <0x18> has no merges.
# Token <0x19> has no merges.
# Token <0x1A> has no merges.
# Token <0x1B> has no merges.
# Token <0x1C> has no merges.
# Token <0x1D> has no merges.
# Token <0x1E> has no merges.
# Token <0x1F> has no merges.
# Token <0x20> has no merges.
# Token <0x21> has no merges.
# Token <0x22> has no merges.
# Token <0x23> has no merges.
# Token <0x24> has no merges.
# Token <0x25> has no merges.
# Token <0x26> has no merges.
# Token <0x27> has no merges.
# Token <0x28> has no merges.
# Token <0x29> has no merges.
# Token <0x2A> has no merges.
# Token <0x2B> has no merges.
# Token <0x2C> has no merges.
# Token <0x2D> has no merges.
# Token <0x2E> has no merges.
# Token <0x2F> has no merges.
# Token <0x30> has no merges.
# Token <0x31> has no merges.
# Token <0x32> has no merges.
# Token <0x33> has no merges.
# Token <0x34> has no merges.
# Token <0x35> has no merges.
# Token <0x36> has no merges.
# Token <0x37> has no merges.
# Token <0x38> has no merges.
# Token <0x39> has no merges.
# Token <0x3A> has no merges.
# Token <0x3B> has no merges.
# Token <0x3C> has no merges.
# Token <0x3D> has no merges.
# Token <0x3E> has no merges.
# Token <0x3F> has no merges.
# Token <0x40> has no merges.
# Token <0x41> has no merges.
# Token <0x42> has no merges.
# Token <0x43> has no merges.
# Token <0x44> has no merges.
# Token <0x45> has no merges.
# Token <0x46> has no merges.
# Token <0x47> has no merges.
# Token <0x48> has no merges.
# Token <0x49> has no merges.
# Token <0x4A> has no merges.
# Token <0x4B> has no merges.
# Token <0x4C> has no merges.
# Token <0x4D> has no merges.
# Token <0x4E> has no merges.
# Token <0x4F> has no merges.
# Token <0x50> has no merges.
# Token <0x51> has no merges.
# Token <0x52> has no merges.
# Token <0x53> has no merges.
# Token <0x54> has no merges.
# Token <0x55> has no merges.
# Token <0x56> has no merges.
# Token <0x57> has no merges.
# Token <0x58> has no merges.
# Token <0x59> has no merges.
# Token <0x5A> has no merges.
# Token <0x5B> has no merges.
# Token <0x5C> has no merges.
# Token <0x5D> has no merges.
# Token <0x5E> has no merges.
# Token <0x5F> has no merges.
# Token <0x60> has no merges.
# Token <0x61> has no merges.
# Token <0x62> has no merges.
# Token <0x63> has no merges.
# Token <0x64> has no merges.
# Token <0x65> has no merges.
# Token <0x66> has no merges.
# Token <0x67> has no merges.
# Token <0x68> has no merges.
# Token <0x69> has no merges.
# Token <0x6A> has no merges.
# Token <0x6B> has no merges.
# Token <0x6C> has no merges.
# Token <0x6D> has no merges.
# Token <0x6E> has no merges.
# Token <0x6F> has no merges.
# Token <0x70> has no merges.
# Token <0x71> has no merges.
# Token <0x72> has no merges.
# Token <0x73> has no merges.
# Token <0x74> has no merges.
# Token <0x75> has no merges.
# Token <0x76> has no merges.
# Token <0x77> has no merges.
# Token <0x78> has no merges.
# Token <0x79> has no merges.
# Token <0x7A> has no merges.
# Token <0x7B> has no merges.
# Token <0x7C> has no merges.
# Token <0x7D> has no merges.
# Token <0x7E> has no merges.
# Token <0x7F> has no merges.
# Token <0x80> has no merges.
# Token <0x81> has no merges.
# Token <0x82> has no merges.
# Token <0x83> has no merges.
# Token <0x84> has no merges.
# Token <0x85> has no merges.
# Token <0x86> has no merges.
# Token <0x87> has no merges.
# Token <0x88> has no merges.
# Token <0x89> has no merges.
# Token <0x8A> has no merges.
# Token <0x8B> has no merges.
# Token <0x8C> has no merges.
# Token <0x8D> has no merges.
# Token <0x8E> has no merges.
# Token <0x8F> has no merges.
# Token <0x90> has no merges.
# Token <0x91> has no merges.
# Token <0x92> has no merges.
# Token <0x93> has no merges.
# Token <0x94> has no merges.
# Token <0x95> has no merges.
# Token <0x96> has no merges.
# Token <0x97> has no merges.
# Token <0x98> has no merges.
# Token <0x99> has no merges.
# Token <0x9A> has no merges.
# Token <0x9B> has no merges.
# Token <0x9C> has no merges.
# Token <0x9D> has no merges.
# Token <0x9E> has no merges.
# Token <0x9F> has no merges.
# Token <0xA0> has no merges.
# Token <0xA1> has no merges.
# Token <0xA2> has no merges.
# Token <0xA3> has no merges.
# Token <0xA4> has no merges.
# Token <0xA5> has no merges.
# Token <0xA6> has no merges.
# Token <0xA7> has no merges.
# Token <0xA8> has no merges.
# Token <0xA9> has no merges.
# Token <0xAA> has no merges.
# Token <0xAB> has no merges.
# Token <0xAC> has no merges.
# Token <0xAD> has no merges.
# Token <0xAE> has no merges.
# Token <0xAF> has no merges.
# Token <0xB0> has no merges.
# Token <0xB1> has no merges.
# Token <0xB2> has no merges.
# Token <0xB3> has no merges.
# Token <0xB4> has no merges.
# Token <0xB5> has no merges.
# Token <0xB6> has no merges.
# Token <0xB7> has no merges.
# Token <0xB8> has no merges.
# Token <0xB9> has no merges.
# Token <0xBA> has no merges.
# Token <0xBB> has no merges.
# Token <0xBC> has no merges.
# Token <0xBD> has no merges.
# Token <0xBE> has no merges.
# Token <0xBF> has no merges.
# Token <0xC0> has no merges.
# Token <0xC1> has no merges.
# Token <0xC2> has no merges.
# Token <0xC3> has no merges.
# Token <0xC4> has no merges.
# Token <0xC5> has no merges.
# Token <0xC6> has no merges.
# Token <0xC7> has no merges.
# Token <0xC8> has no merges.
# Token <0xC9> has no merges.
# Token <0xCA> has no merges.
# Token <0xCB> has no merges.
# Token <0xCC> has no merges.
# Token <0xCD> has no merges.
# Token <0xCE> has no merges.
# Token <0xCF> has no merges.
# Token <0xD0> has no merges.
# Token <0xD1> has no merges.
# Token <0xD2> has no merges.
# Token <0xD3> has no merges.
# Token <0xD4> has no merges.
# Token <0xD5> has no merges.
# Token <0xD6> has no merges.
# Token <0xD7> has no merges.
# Token <0xD8> has no merges.
# Token <0xD9> has no merges.
# Token <0xDA> has no merges.
# Token <0xDB> has no merges.
# Token <0xDC> has no merges.
# Token <0xDD> has no merges.
# Token <0xDE> has no merges.
# Token <0xDF> has no merges.
# Token <0xE0> has no merges.
# Token <0xE1> has no merges.
# Token <0xE2> has no merges.
# Token <0xE3> has no merges.
# Token <0xE4> has no merges.
# Token <0xE5> has no merges.
# Token <0xE6> has no merges.
# Token <0xE7> has no merges.
# Token <0xE8> has no merges.
# Token <0xE9> has no merges.
# Token <0xEA> has no merges.
# Token <0xEB> has no merges.
# Token <0xEC> has no merges.
# Token <0xED> has no merges.
# Token <0xEE> has no merges.
# Token <0xEF> has no merges.
# Token <0xF0> has no merges.
# Token <0xF1> has no merges.
# Token <0xF2> has no merges.
# Token <0xF3> has no merges.
# Token <0xF4> has no merges.
# Token <0xF5> has no merges.
# Token <0xF6> has no merges.
# Token <0xF7> has no merges.
# Token <0xF8> has no merges.
# Token <0xF9> has no merges.
# Token <0xFA> has no merges.
# Token <0xFB> has no merges.
# Token <0xFC> has no merges.
# Token <0xFD> has no merges.
# Token <0xFE> has no merges.
# Token <0xFF> has no merges.
# Traceback (most recent call last):
#   File "/home/miro/PycharmProjects/NLP/distilintent/distill.py", line 17, in <module>
#     m2v_model = distill(model_name=m, pca_dims=256)
#   File "/home/miro/PycharmProjects/NLP/.venv/lib/python3.13/site-packages/model2vec/distill/distillation.py", line 239, in distill
#     return distill_from_model(
#         model=model,
#     ...<8 lines>...
#         use_subword=use_subword,
#     )
#   File "/home/miro/PycharmProjects/NLP/.venv/lib/python3.13/site-packages/model2vec/distill/distillation.py", line 109, in distill_from_model
#     backend_tokenizer = replace_vocabulary(backend_tokenizer, all_tokens, unk_token=unk_token, pad_token=pad_token)
#   File "/home/miro/PycharmProjects/NLP/.venv/lib/python3.13/site-packages/model2vec/distill/tokenizer.py", line 180, in replace_vocabulary
#     return Tokenizer.from_str(json.dumps(tokenizer_json))
#            ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Exception: Token `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` out of vocabulary at line 1 column 22001662