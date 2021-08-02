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

Use the *#track-5-numerical* slack channel for general help and it support.

<center style="font-size:18px">Launch #track-5-numerical Slack in<br><a href="{{vroom.slackweb}}" onclick="window.open(this.href,'newwindow','width=600,height=900'); return false;">new browser window</a> or <a href="{{vroom.slackapp}}">desktop app</a></center>

As a last resort, you can try emailing...

* [Satish Balay](<mailto:balay@mcs.anl.gov>),
* [Cameron Smith](<mailto:smithc11@rpi.edu>)
* [Alp Dener](<mailto:adener@anl.gov>)

{% include link-shortcuts %}
