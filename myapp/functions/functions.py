import chunk


def uploded_file_fn(f):
    with open('media/videos/'+f.name ,'wb+') as destinations:
        for chunk in f.chunks():
            destinations.write(chunk)

