import torch
from transformers import BertTokenizer, BertModel, BertForMaskedLM

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
#model.eval()

def fillInTheBlanks(sentence, topK):
  #Convert to BERT format
  #NOTE: This must be done for every sentence. As an assignment, you can try to change this to reflect multiple sentences.
  text = "[CLS]" + sentence + "[SEP]"
  tokenizedText = tokenizer.tokenize(text)
  maskedIndex = tokenizedText.index("[MASK]")
  indexedTokens = tokenizer.convert_tokens_to_ids(tokenizedText)
  tokensTensor = torch.tensor([indexedTokens])
  #print(tokensTensor)
  with torch.no_grad():
    outputs = model(tokensTensor)
    predictions = outputs[0]
    #print(predictions)

  probabilities = torch.nn.functional.softmax(predictions[0, maskedIndex], dim=-1)
  topKWeights, topKIndices = torch.topk(probabilities, topK, sorted=True)

  for i, predictionIndex in enumerate(topKIndices):
    predictedToken = tokenizer.convert_ids_to_tokens([predictionIndex])[0]
    tokenWeight = topKWeights[i]
    print("[MASK]: ", predictedToken, "| weight = ", float(tokenWeight))

fillInTheBlanks("The sky is [MASK] and the sea is [MASK].", topK=2)