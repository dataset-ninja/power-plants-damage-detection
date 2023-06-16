Dataset **Damage Detection of Power Plants** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/6/0/Tm/sTifj5UUfAuPTp2Pb9RROdj9sEf7TfVZ1CEKsx8QdHz883bA15f5uPrVBxpBkJ1F0RhYZokUDd5RGvKhEo1vppj33xXaFYKWqRS6m0OkGkfenK0bJXjwieyTdOgp.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Damage Detection of Power Plants', dst_path='~/dtools/datasets/Damage Detection of Power Plants.tar')
```
The data in original format can be 🔗[downloaded here](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW#)