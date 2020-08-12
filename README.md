Willem's COVID processing code.

Needs the data from https://github.com/datasets/covid-19 to be stored at ../covid-19/data

#===================================

Coronavirus disease 2019 (COVID-19) time series listing confirmed cases, reported deaths and reported recoveries. Data is disaggregated by country (and sometimes subregion). Coronavirus disease (COVID-19) is caused by the [Severe acute respiratory syndrome Coronavirus 2 (SARS-CoV-2)][sars2] and has had a worldwide effect. On March 11 2020, the World Health Organization (WHO) declared it a pandemic, pointing to the over 118,000 cases of the Coronavirus illness in over 110 countries and territories around the world at the time.

[covid]: https://en.wikipedia.org/wiki/Coronavirus_disease_2019
[sars2]: https://en.wikipedia.org/wiki/Severe_acute_respiratory_syndrome_coronavirus_2

This dataset includes time series data tracking the number of people affected by COVID-19 worldwide, including:

* confirmed tested cases of Coronavirus infection
* the number of people who have reportedly died while sick with Coronavirus
* the number of people who have reportedly recovered from it

## Data

Data is in CSV format and updated daily. It is sourced from [this upstream repository](https://github.com/CSSEGISandData/COVID-19) maintained by the amazing team at [Johns Hopkins University Center for Systems Science and Engineering](https://systems.jhu.edu/) (CSSE) who have been doing a great public service from an early point by collating data from around the world.

We have cleaned and normalized that data, for example tidying dates and consolidating several files into normalized time series. We have also added some metadata such as column descriptions and [data packaged it][dp].

You can view the data, its structure as well as download it in alternative formats (e.g. JSON) from the DataHub:

https://datahub.io/core/covid-19

[dp]: https://frictionlessdata.io/data-package/

## License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/

The data comes from a variety public sources and was collated in the first instance via Johns Hopkins University on GitHub. We have used that data and processed it further. Given the public sources and factual nature we believe that there the data is public domain and are therefore releasing the results under the Public Domain Dedication and License. We are also, of course, explicitly licensing any contribution of ours under that license.

