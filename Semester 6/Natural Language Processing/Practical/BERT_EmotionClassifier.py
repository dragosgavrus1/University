from torch import nn, optim
from transformers import XLMRobertaModel

class EmotionsClassifier(nn.Module):
    def __init__(self, n_classes, model_name):
        super(EmotionsClassifier, self).__init__()
        self.roberta = XLMRobertaModel.from_pretrained(model_name)
        self.drop = nn.Dropout(p=0.3)
        self.out = nn.Linear(self.roberta.config.hidden_size, n_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.roberta(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=True
        )
        pooled_output = outputs.pooler_output if outputs.pooler_output is not None else outputs.last_hidden_state[:, 0]
        output = self.drop(pooled_output)
        return self.out(output)
