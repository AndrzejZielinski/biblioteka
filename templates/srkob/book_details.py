{% extends 'srkob/base.html' %}

{% load static %}

{% block title %}Książki{% endblock%}


{% block nav_body %}{% endblock %}
{% block body_block %}
        <h1>{{ genre_name }}</h1>
        {% if books %}
            <ul>
                {% for book in books %}
                <li>{{ book.title }}</a></li>
                {% endfor %}
            </ul>
            {% else %}
                <strong>No pages currently in category.</strong>
            {% endif %}
        {% else %}
            The specified category {{ category_name }} does not exist!
        {% endif %}
{% endblock %} 
