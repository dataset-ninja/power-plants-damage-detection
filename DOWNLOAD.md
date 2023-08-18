Dataset **Damage Detection of Power Plants** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/y/9/5H/qTa1Ng1Lzwu8QO8u7ENy95djFaZiNjf3cUxERgILoBDXqdzqk5FdjaOZeZ47BlhWOEOt9ktGvJaWpEVVjiYGmL9gc6cIuPrRED2BmVc5lXyzVhK8KePMiz8cYZWG.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Damage Detection of Power Plants', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Solar_large.rar](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW#)
- [Solar_small.rar](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW#)
- [Solar_small_IR.rar](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW#)
- [Wind.rar](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW#)
