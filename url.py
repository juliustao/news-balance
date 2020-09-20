# site partisanship is according to AllSides.com

left_wing = {
    "abcnews.go.com",
    "www.alternet.org",
    "apnews.com",
    "www.bloomberg.com",
    "www.buzzfeednews.com",
    "www.cbsnews.com",
    "www.cnn.com",
    "www.thedailybeast.com",
    "www.democracynow.org",
    "www.huffpost.com",
    "www.motherjones.com",
    "www.msnbc.com",
    "www.nbcnews.com",
    "www.nytimes.com",
    "www.politico.com",
    "slate.com",
    "www.theatlantic.com",
    "www.economist.com",
    "www.theguardian.com",
    "theintercept.com",
    "www.newyorker.com",
    "time.com",
    "www.vox.com",
    "www.washingtonpost.com",
}

right_wing = {
    "www.breitbart.com",
    "www.dailymail.co.uk",
    "www.foxnews.com",
    "www.nationalreview.com",
    "nypost.com",
    "reason.com",
    "spectator.org",
    "dailycaller.com",
    "www.dailywire.com",
    "thefederalist.com",
    "www.theblaze.com",
    "www.washingtonexaminer.com",
    "www.washingtontimes.com",
}


def get_view(site):
    if site in left_wing:
        return "left"
    elif site in right_wing:
        return "right"
    else:
        return None
