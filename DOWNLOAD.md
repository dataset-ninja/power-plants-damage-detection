Dataset **Damage Detection of Power Plants** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTQ2OV9EYW1hZ2UgRGV0ZWN0aW9uIG9mIFBvd2VyIFBsYW50cy9kYW1hZ2UtZGV0ZWN0aW9uLW9mLXBvd2VyLXBsYW50cy1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJDeHozNzhhenJQZzY3SDY5NkxOYmlWMFJRQ1lqQ1dVUGJXdklQVnhjWWhVPSJ9?response-content-disposition=attachment%3B%20filename%3D%22damage-detection-of-power-plants-DatasetNinja.tar%22)

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
