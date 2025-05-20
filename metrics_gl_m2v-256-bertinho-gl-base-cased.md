# Model Evaluation Metrics Summary
## galician - Model: Jarbas/m2v-256-bertinho-gl-base-cased
### Accuracy: 0.9862187769164513
### F1 Score: 0.9844960738762856
### Cohen Kappa Score: 0.9848588834241615
### Matthews Corrcoef Score: 0.9848709253545295
### Classification Report:
```
                                                                        precision    recall  f1-score   support

                                             common_query:common_query       1.00      1.00      1.00         5
                    ovos-skill-alerts.openvoiceos:missed_alerts.intent       1.00      1.00      1.00        10
         ovos-skill-audio-recording.openvoiceos:start_recording.intent       0.94      1.00      0.97        15
ovos-skill-boot-finished.openvoiceos:disable_ready_notification.intent       1.00      1.00      1.00        30
 ovos-skill-boot-finished.openvoiceos:enable_ready_notification.intent       0.97      1.00      0.98        30
           ovos-skill-date-time.openvoiceos:date.future.weekend.intent       1.00      1.00      1.00        15
             ovos-skill-date-time.openvoiceos:date.last.weekend.intent       1.00      1.00      1.00        10
                ovos-skill-date-time.openvoiceos:what.day.is.it.intent       1.00      1.00      1.00         1
              ovos-skill-date-time.openvoiceos:what.month.is.it.intent       1.00      1.00      1.00         2
               ovos-skill-date-time.openvoiceos:what.time.is.it.intent       0.93      1.00      0.97        14
          ovos-skill-date-time.openvoiceos:what.time.will.it.be.intent       1.00      1.00      1.00         4
            ovos-skill-date-time.openvoiceos:what.weekday.is.it.intent       1.00      1.00      1.00         1
               ovos-skill-date-time.openvoiceos:what.year.is.it.intent       1.00      1.00      1.00         2
        ovos-skill-days-in-history.openvoiceos:today_in_history.intent       1.00      1.00      1.00         7
                         ovos-skill-ddg.openvoiceos:search_duck.intent       1.00      1.00      1.00         2
             ovos-skill-diagnostics.openvoiceos:query_cpu_usage.intent       1.00      1.00      1.00         1
           ovos-skill-diagnostics.openvoiceos:query_extra_langs.intent       1.00      1.00      1.00         1
                   ovos-skill-diagnostics.openvoiceos:query_gpu.intent       1.00      1.00      1.00         1
        ovos-skill-diagnostics.openvoiceos:query_kernel_version.intent       1.00      1.00      1.00         1
                 ovos-skill-diagnostics.openvoiceos:query_langs.intent       1.00      1.00      1.00         2
          ovos-skill-diagnostics.openvoiceos:query_memory_usage.intent       1.00      1.00      1.00         1
         ovos-skill-diagnostics.openvoiceos:query_ovos_location.intent       1.00      1.00      1.00         1
          ovos-skill-diagnostics.openvoiceos:query_primary_lang.intent       1.00      1.00      1.00         2
             ovos-skill-diagnostics.openvoiceos:query_user_lang.intent       1.00      1.00      1.00         2
         ovos-skill-diagnostics.openvoiceos:query_user_location.intent       0.00      0.00      0.00         1
               ovos-skill-dictation.openvoiceos:start_dictation.intent       1.00      1.00      1.00        26
                ovos-skill-dictation.openvoiceos:stop_dictation.intent       1.00      1.00      1.00        11
                   ovos-skill-hello-world.openvoiceos:Greetings.intent       0.67      0.67      0.67         6
                            ovos-skill-ip.openvoiceos:what.ssid.intent       1.00      1.00      1.00         2
                      ovos-skill-iss-location.openvoiceos:about.intent       1.00      1.00      1.00         2
                   ovos-skill-iss-location.openvoiceos:when_iss.intent       1.00      1.00      1.00         8
                  ovos-skill-iss-location.openvoiceos:where_iss.intent       1.00      1.00      1.00         3
                             ovos-skill-laugh.openvoiceos:Laugh.intent       1.00      1.00      1.00         3
                       ovos-skill-laugh.openvoiceos:RandomLaugh.intent       1.00      1.00      1.00         2
          ovos-skill-moviemaster.openvoiceos:genre.movie.search.intent       0.00      0.00      0.00         2
             ovos-skill-moviemaster.openvoiceos:genre.tv.search.intent       1.00      1.00      1.00         5
                  ovos-skill-moviemaster.openvoiceos:movie.cast.intent       1.00      1.00      1.00         2
           ovos-skill-moviemaster.openvoiceos:movie.description.intent       1.00      1.00      1.00         4
          ovos-skill-moviemaster.openvoiceos:movie.genre.search.intent       0.60      0.75      0.67         4
                ovos-skill-moviemaster.openvoiceos:movie.genres.intent       1.00      1.00      1.00         7
           ovos-skill-moviemaster.openvoiceos:movie.information.intent       1.00      1.00      1.00        36
               ovos-skill-moviemaster.openvoiceos:movie.popular.intent       1.00      1.00      1.00         7
            ovos-skill-moviemaster.openvoiceos:movie.production.intent       1.00      1.00      1.00         1
       ovos-skill-moviemaster.openvoiceos:movie.recommendations.intent       1.00      1.00      1.00         8
               ovos-skill-moviemaster.openvoiceos:movie.runtime.intent       1.00      1.00      1.00         2
                   ovos-skill-moviemaster.openvoiceos:movie.top.intent       1.00      1.00      1.00        22
                  ovos-skill-moviemaster.openvoiceos:movie.year.intent       1.00      1.00      1.00         4
                         ovos-skill-naptime.openvoiceos:naptime.intent       1.00      1.00      1.00         6
                        ovos-skill-news.openvoiceos:global_news.intent       0.94      1.00      0.97        16
                               ovos-skill-news.openvoiceos:news.intent       0.98      0.98      0.98        63
                  ovos-skill-parrot.openvoiceos:did.you.hear.me.intent       1.00      1.00      1.00         2
                       ovos-skill-parrot.openvoiceos:repeat.stt.intent       1.00      1.00      1.00         1
                       ovos-skill-parrot.openvoiceos:repeat.tts.intent       1.00      0.67      0.80         3
                            ovos-skill-parrot.openvoiceos:speak.intent       1.00      1.00      1.00         1
                     ovos-skill-parrot.openvoiceos:start_parrot.intent       1.00      0.50      0.67         2
                      ovos-skill-parrot.openvoiceos:stop_parrot.intent       0.80      1.00      0.89         4
                     ovos-skill-personal.openvoiceos:WhatAreYou.intent       1.00      1.00      1.00         3
                ovos-skill-personal.openvoiceos:WhenWereYouBorn.intent       1.00      1.00      1.00         2
               ovos-skill-personal.openvoiceos:WhereWereYouBorn.intent       0.67      1.00      0.80         2
                      ovos-skill-personal.openvoiceos:WhoAreYou.intent       0.00      0.00      0.00         1
                     ovos-skill-personal.openvoiceos:WhoMadeYou.intent       1.00      1.00      1.00         5
               ovos-skill-randomness.openvoiceos:fortune-teller.intent       1.00      1.00      1.00         2
                ovos-skill-randomness.openvoiceos:pick-a-number.intent       1.00      1.00      1.00         1
           ovos-skill-randomness.openvoiceos:roll-multiple-dice.intent       1.00      1.00      1.00         1
              ovos-skill-randomness.openvoiceos:roll-single-die.intent       1.00      1.00      1.00         1
                   ovos-skill-volume.openvoiceos:volume.default.intent       1.00      1.00      1.00         1
                      ovos-skill-volume.openvoiceos:volume.high.intent       1.00      1.00      1.00         1
                       ovos-skill-volume.openvoiceos:volume.low.intent       1.00      1.00      1.00         1
                       ovos-skill-volume.openvoiceos:volume.max.intent       1.00      1.00      1.00         1
                      ovos-skill-volume.openvoiceos:volume.mute.intent       1.00      1.00      1.00         1
                    ovos-skill-volume.openvoiceos:volume.unmute.intent       0.00      0.00      0.00         1
                 ovos-skill-weather.openvoiceos:N_days_forecast.intent       1.00      1.00      1.00        10
             ovos-skill-weather.openvoiceos:current_temperature.intent       1.00      1.00      1.00        13
                 ovos-skill-weather.openvoiceos:current_weather.intent       0.89      1.00      0.94         8
                  ovos-skill-weather.openvoiceos:daily_forecast.intent       1.00      0.99      0.99        75
                ovos-skill-weather.openvoiceos:high_temperature.intent       1.00      1.00      1.00        41
                 ovos-skill-weather.openvoiceos:hourly_forecast.intent       1.00      1.00      1.00       291
              ovos-skill-weather.openvoiceos:hourly_temperature.intent       1.00      1.00      1.00       127
                        ovos-skill-weather.openvoiceos:humidity.intent       1.00      1.00      1.00         5
                        ovos-skill-weather.openvoiceos:is_clear.intent       1.00      1.00      1.00        11
                          ovos-skill-weather.openvoiceos:is_fog.intent       1.00      1.00      1.00         7
                         ovos-skill-weather.openvoiceos:is_rain.intent       0.82      1.00      0.90        14
                         ovos-skill-weather.openvoiceos:is_snow.intent       1.00      0.83      0.91         6
                       ovos-skill-weather.openvoiceos:is_stormy.intent       1.00      0.71      0.83         7
                         ovos-skill-weather.openvoiceos:is_wind.intent       1.00      1.00      1.00        12
                 ovos-skill-weather.openvoiceos:low_temperature.intent       1.00      1.00      1.00        40
                       ovos-skill-weather.openvoiceos:next_rain.intent       1.00      1.00      1.00         2
                         ovos-skill-weather.openvoiceos:sunrise.intent       1.00      0.75      0.86         4
                          ovos-skill-weather.openvoiceos:sunset.intent       1.00      1.00      1.00         4
                ovos-skill-weather.openvoiceos:weekend_forecast.intent       1.00      1.00      1.00        13
                         ovos-skill-wikihow.openvoiceos:wikihow.intent       1.00      1.00      1.00         2
                          ovos-skill-wikipedia.openvoiceos:wiki.intent       1.00      1.00      1.00         8
                  ovos-skill-wikipedia.openvoiceos:wikiroulette.intent       1.00      1.00      1.00         3
                    ovos-skill-wolfie.openvoiceos:search_wolfie.intent       1.00      1.00      1.00         2
                         ovos-skill-wordnet.openvoiceos:antonym.intent       1.00      1.00      1.00         1
                         ovos-skill-wordnet.openvoiceos:holonym.intent       1.00      1.00      1.00         1
                        ovos-skill-wordnet.openvoiceos:hypernym.intent       1.00      1.00      1.00         1
                         ovos-skill-wordnet.openvoiceos:hyponym.intent       1.00      1.00      1.00         1
                           ovos-skill-wordnet.openvoiceos:lemma.intent       1.00      1.00      1.00         1
                  ovos-skill-wordnet.openvoiceos:search_wordnet.intent       1.00      1.00      1.00         1

                                                              accuracy                           0.99      1161
                                                             macro avg       0.94      0.94      0.94      1161
                                                          weighted avg       0.98      0.99      0.98      1161

```

