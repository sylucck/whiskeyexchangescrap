from django.test import TestCase

# Create your tests here.

<div class="row">
    {% for post in final_postings %}
        <div class="col s4">
            <div class="card">
                <div class="card-image">
                    <a href="{{ post.1 }}"><img src="{{ post.3 }}" alt=""></a>
                </div>
                <div class="card-content">
                    <p>{{ post.0 }}</p>
                </div>
                <div class="card-action">
                    <a href="{{ post.1 }}">View listing: Price {{ post.2 }}</a>
                </div>
            </div>
        </div>
    {% endfor %}
</div>