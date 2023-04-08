from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from streaming.models import Movie, UserProfile

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    sorted_movies = sorted(movies, key=lambda movie: movie.average_rating() if isinstance(movie.average_rating(), float) else 0, reverse=True)
    return render(request, 'streaming/index.html', {'movies': sorted_movies})

def movie(request, movie_id):
    try:
        print(Movie.objects.get(pk=movie_id))
        movie = Movie.objects.get(pk=movie_id)
        return render(request, 'streaming/movie.html', {'movie': movie})
    except ObjectDoesNotExist:
        raise Http404('Movie not found')


# Other views here...

def user_reviews(request, user_id):
    user_profile = get_object_or_404(UserProfile, id=user_id)
    reviews = user_profile.reviews.all()
    return render(request, 'streaming/user_reviews.html', {'user_profile': user_profile, 'reviews': reviews})

from django.shortcuts import render
from .models import Movie, SubscriptionPlan

def subscription_plan(request, subscription_id):
    subscription = SubscriptionPlan.objects.get(pk=subscription_id)
    movies = Movie.objects.all()
    return render(request, 'streaming/subscription_plan.html', {'movies': movies, 'subscription': subscription})

