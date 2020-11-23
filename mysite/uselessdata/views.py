from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from uselessdata.models import Blogs, Comments, Contacts
from datetime import datetime as dt
import random

def index(request):
    return render(request,'index.html')

def getasList(r1, r2):
    if (r1 == r2): 
        return [r1]
    else: 
        res = [] 
        while(r1 < r2+1 ):
            res.append(r1) 
            r1 += 1
        return res 

def merger(d, w, m):
	l = []
	for i in range(len(d)):
		l.append([m[i], w[i], d[i]])
	return l

def experiments(request):
	all_blogs = Blogs.objects.all()
	sdates = [all_blogs[s].start_date for s in range(len(all_blogs))]
	edates = [all_blogs[e].end_date for e in range(len(all_blogs))]
	d = [int(str((dt.strptime(str(edates[i])[:10], "%Y-%m-%d")-dt.strptime(str(sdates[i])[:10], "%Y-%m-%d")).days))+1 for i in range(len(all_blogs))]
	w = [0] * len(all_blogs)
	m = [0] * len(all_blogs)
	
	for i in range(len(all_blogs)):
		if d[i] >= 30:
			m[i] = int(d[i]/30)
			d[i] %= 30
		if d[i] >= 7:
			w[i] = int(d[i]/7)
			d[i] %= 7
	
	days = [getasList(1, i) for i in d]
	weeks = [getasList(1, i) for i in w]
	months = [getasList(1, i) for i in m]

	mergedList = merger(days, weeks, months)

	json = {
		'all_blogs': all_blogs,
		'merged': mergedList
	}

	return render(request, 'experiments.html', json, content_type=RequestContext(request))

@csrf_exempt
def blog1(request):
	if request.method=='POST':
		name = request.POST.get("name") if request.POST.get("name") else 0
		comment = request.POST.get("comment")
		all_blogs = Blogs.objects.get(bid=1)
		c = Comments(username=name,cdesc=comment,bid=all_blogs) if name else Comments(cdesc=comment,bid=all_blogs)
		c.save()
		return HttpResponseRedirect('success1')
	all_blogs = Blogs.objects.get(bid=1)
	all_comments = Comments.objects.filter(bid=all_blogs)
	gif_type = random.randint(1,2)
	gif = random.randint(1,11)
	gif_links = ['https://media.giphy.com/media/CaiVJuZGvR8HK/source.gif','https://media.giphy.com/media/EJIFaXV55556M/source.gif','https://media.giphy.com/media/Jk4ZT6R0OEUoM/source.gif','https://media.giphy.com/media/3owypf6HrM3J7UTvAA/source.gif','https://media.giphy.com/media/tPsWbNw7homfm/source.gif','https://media.giphy.com/media/JWeOLmnFvLYB2/source.gif','https://media.giphy.com/media/PKgfwX7ct5f5C/giphy.gif','https://media.giphy.com/media/G8E0raYJHQDVC/source.gif','https://media.giphy.com/media/csXqmaigJhqQU/source.gif','https://media.giphy.com/media/8TL7DBsPtEXqo/source.gif','https://media.giphy.com/media/9r8BF7Cdjkr0f4LLXF/source.gif']

	glink = gif_links[gif-1] if gif_type == 1 else str(gif) + '.gif'
	
	json = {
		'comments': all_comments,
		'gif_type': gif_type,
		'glink': glink,
		'num_of_comments': len(all_comments)
	}

	return render(request,'blog1.html', json, content_type=RequestContext(request))

@csrf_exempt
def blog2(request):
	if request.method=='POST':
		name = request.POST.get("name") if request.POST.get("name") else 0
		comment = request.POST.get("comment")
		all_blogs = Blogs.objects.get(bid=2)
		if not name:
			name = ''
			salutation = ['Mr.', 'Mrs.', 'Dr.', 'The', 'Sir', 'Prof.', "Ma'am", 'Your', 'My', 'Lord', 'Super', 'Anti', 'Unreal', 'Unsuccessful']
			firstnames = ['Awesome', 'Amazing', 'Kidney', 'Liquid', 'Psycho', 'Banana', 'Barbie', 'Macho', 'Panda', 'Hammer', 'Black', 'Hair', 'Saliva', 'Princess', 'Dusty', 'Dirty', 'Naughty', 'Lazy', 'White', 'Noob', 'Purple', 'Magical', 'Rosy', 'Photosynthesized', 'Cheesy', 'Egoist', 'Cookie', 'Ice Cream', 'Fluffy', 'Infinite', 'Vegan', 'Burger', 'Flappy', 'Hairy', 'Theoretical', 'Useless', 'Muscular', 'Morty', 'Pickle', 'Edible', 'Bioderadable', 'Nonbioderadable', 'Recycled', 'Reused', 'Lentil', 'Carrot', 'Cereal', 'Digested', 'Avocado', 'Beetroot', 'Stoned']
			lastnames = ['Smasher', 'Drinker', 'Phagocyter', 'Smashed', 'Philosopher', 'Smell', 'Plucker', 'Licker', 'Scratcher', 'Potter', 'Princess', 'Unicorn', 'Extractor', 'Hugger', 'Photosynthesizer', 'Sanitizer', 'Pad', 'Respirator', 'Ice Cream', 'King', 'Queen', 'Physicist', 'Scientist', 'Lover', 'Morty', 'Chewer', 'Eater', 'Man', 'Woman', 'God', 'Goddess', 'Feminist', 'Chemist', 'Cryptocurrency', 'Bamboo', 'Sniffer', 'Mosquito', 'Make-up', 'Rick', 'Brother', 'Sister', 'Digestion', 'Shape', 'Maker', 'Dominator', 'Rapper', 'Influencer', 'Toe']
			fullnames = ['Michael Jackson', 'Donald Trump', 'The Little Mermaid', 'Ronald McDonald', 'Burger King', 'Mr. Bean', 'Harry Potter', 'Stephan Hawking', 'Carl Sagan']
			fn = False
			odds = random.randint(1,5)
			if odds == 1:
				name += salutation[random.randint(0,len(salutation))] + ' '
			odds = random.randint(1,6)
			if odds == 1:
				name += fullnames[random.randint(0,len(fullnames))]
				fn = True
			if not fn:
				name += firstnames[random.randint(0,len(fullnames))] + ' ' + firstnames[random.randint(0,len(fullnames))]
		c = Comments(username=name,cdesc=comment,bid=all_blogs)
		c.save()
		return HttpResponseRedirect('success2')
	all_blogs = Blogs.objects.get(bid=2)
	all_comments = Comments.objects.filter(bid=all_blogs)
	gif_type = random.randint(1,2)
	gif = random.randint(1,11)
	gif_links = ['https://media.giphy.com/media/CaiVJuZGvR8HK/source.gif','https://media.giphy.com/media/EJIFaXV55556M/source.gif','https://media.giphy.com/media/Jk4ZT6R0OEUoM/source.gif','https://media.giphy.com/media/3owypf6HrM3J7UTvAA/source.gif','https://media.giphy.com/media/tPsWbNw7homfm/source.gif','https://media.giphy.com/media/JWeOLmnFvLYB2/source.gif','https://media.giphy.com/media/PKgfwX7ct5f5C/giphy.gif','https://media.giphy.com/media/G8E0raYJHQDVC/source.gif','https://media.giphy.com/media/csXqmaigJhqQU/source.gif','https://media.giphy.com/media/8TL7DBsPtEXqo/source.gif','https://media.giphy.com/media/9r8BF7Cdjkr0f4LLXF/source.gif']

	glink = gif_links[gif-1] if gif_type == 1 else str(gif) + '.gif'
	
	json = {
		'comments': all_comments,
		'gif_type': gif_type,
		'glink': glink,
		'num_of_comments': len(all_comments)
	}

	return render(request,'blog2-activities.html', json, content_type=RequestContext(request))

def success1(request):
	return redirect('/experiments/effects-of-gravity-on-height/')

def success2(request):
	return redirect('/experiments/life-spent-on-daily-activities/')

@csrf_exempt
def contact(request):
	if request.method=='POST':
		cname = request.POST.get("cname") if request.POST.get("cname") else 0
		message = request.POST.get("message")
		email = request.POST.get("email")
		all_blogs = Blogs.objects.get(bid=1)
		c = Contacts(cname=cname,message=message,email=email) if cname else Contacts(message=message,email=email)
		c.save()
		return HttpResponseRedirect('recorded')
	return render(request,'contact-us.html')

def recorded(request):
	return render(request,'recorded.html')

def bets(request):
	return render(request,'bets.html')