TODO: 
======
- [x] load Movies model object / db with IMDB api
- [x] make login/ register form work
- [x] create specific movie page with url pattern /movie-id/
- [ ] create admin dashboard for editing and selecting homepage movies
- [ ] create admin dashboard for editing hall, movie_schedule
- [ ] create search, that supports filtering with name, genre, actors, language, director
- [ ] create dynaimc ticket booking system
- [ ] add movies through json

optional:
- [ ] add functional comment section and user review page for specific movie
- [ ] add movies through api


        ux:
        home page ──► login/signup ──►  specific movie page   ──┐
         │ │                  ▲                                 ▼
         │ └─► select movie ──┘                       select movie schedule 
         ▼              ▲                                       │          
         search movie ──┘  your-tickets ◄─── select seat/book ◄─┘


        admin dashboard
        select 6 movies for home page sidescroller:
        select 12 other movies for display.
        rule for premium/ non premium seat
