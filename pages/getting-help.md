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

Use the *#help-desk* slack channel for general help and it support.

<center style="font-size:18px">Launch #help-desk Slack in<br><a href="https://app.slack.com/client/TMW2FLNCQ/C029TG2QCM8" onclick="window.open(this.href,'newwindow','width=600,height=900'); return false;">new browser window</a> or <a href="slack://channel?team=MW2FLNCQ&id=029TG2QCM8">desktop app</a></center>

Use the *#track-5-numerical* slack channel for help with Track 5 sessions.

<center style="font-size:18px">Launch #track-5-numerical Slack in<br><a href="{{vroom.slackweb}}" onclick="window.open(this.href,'newwindow','width=600,height=900'); return false;">new browser window</a> or <a href="{{vroom.slackapp}}">desktop app</a></center>

As a last resort, you can try emailing...

* [Satish Balay](<mailto:balay@mcs.anl.gov>),
* [Alp Dener](<mailto:adener@anl.gov>)

{% include link-shortcuts %}
