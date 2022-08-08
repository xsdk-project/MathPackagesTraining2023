---
layout: page
show_meta: false
title: "Getting help"
header:
   image_fullwidth: "tech_support8.jpg"
permalink: "/getting-help/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == "Amphitheater" %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

SLACK ALCF-Workshops workspace provides channles for help

* [#help-desk-general](https://alcf-workshops.slack.com/archives/C03QPJSUL90)
* [#track-5-numerical](https://alcf-workshops.slack.com/archives/C03Q8QEJF6K)

{% include link-shortcuts %}
