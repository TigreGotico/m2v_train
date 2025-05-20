# Model Evaluation Metrics Summary
## portuguese - Model: Jarbas/m2v-256-albertina-100m-portuguese-ptpt-encoder
### Accuracy: 0.9718969555035128
### F1 Score: 0.9674229623065551
### Cohen Kappa Score: 0.9703025385417874
### Matthews Corrcoef Score: 0.9703756843554464
### Classification Report:
```
                                                                        precision    recall  f1-score   support

                                             common_query:common_query       0.86      1.00      0.92         6
                         ovos-skill-alerts.openvoiceos:AddListSubitems       1.00      0.50      0.67         2
                             ovos-skill-alerts.openvoiceos:CancelAlert       1.00      1.00      1.00         1
                             ovos-skill-alerts.openvoiceos:CreateAlarm       1.00      1.00      1.00         2
                              ovos-skill-alerts.openvoiceos:CreateList       1.00      1.00      1.00         1
                          ovos-skill-alerts.openvoiceos:CreateReminder       1.00      1.00      1.00         1
                       ovos-skill-alerts.openvoiceos:DeleteListEntries       1.00      1.00      1.00         1
                       ovos-skill-alerts.openvoiceos:DeleteTodoEntries       1.00      1.00      1.00         1
                              ovos-skill-alerts.openvoiceos:ListAlerts       1.00      1.00      1.00         2
                        ovos-skill-alerts.openvoiceos:QueryListEntries       0.00      0.00      0.00         0
                    ovos-skill-alerts.openvoiceos:missed_alerts.intent       1.00      1.00      1.00        25
         ovos-skill-audio-recording.openvoiceos:start_recording.intent       0.92      1.00      0.96        12
ovos-skill-boot-finished.openvoiceos:disable_ready_notification.intent       1.00      1.00      1.00        20
 ovos-skill-boot-finished.openvoiceos:enable_ready_notification.intent       1.00      1.00      1.00        24
                      ovos-skill-camera.openvoiceos:have_camera.intent       1.00      0.50      0.67         2
           ovos-skill-date-time.openvoiceos:date.future.weekend.intent       1.00      1.00      1.00         9
             ovos-skill-date-time.openvoiceos:date.last.weekend.intent       1.00      1.00      1.00         3
              ovos-skill-date-time.openvoiceos:weekday.for.date.intent       1.00      1.00      1.00         2
               ovos-skill-date-time.openvoiceos:what.time.is.it.intent       1.00      1.00      1.00         5
          ovos-skill-date-time.openvoiceos:what.time.will.it.be.intent       1.00      1.00      1.00         5
            ovos-skill-date-time.openvoiceos:what.weekday.is.it.intent       1.00      1.00      1.00         2
        ovos-skill-days-in-history.openvoiceos:today_in_history.intent       1.00      1.00      1.00        37
                         ovos-skill-ddg.openvoiceos:search_duck.intent       1.00      1.00      1.00         2
             ovos-skill-diagnostics.openvoiceos:query_cpu_usage.intent       0.33      1.00      0.50         1
           ovos-skill-diagnostics.openvoiceos:query_extra_langs.intent       0.33      0.50      0.40         2
                   ovos-skill-diagnostics.openvoiceos:query_gpu.intent       1.00      1.00      1.00         1
        ovos-skill-diagnostics.openvoiceos:query_kernel_version.intent       1.00      1.00      1.00         1
                 ovos-skill-diagnostics.openvoiceos:query_langs.intent       0.80      0.67      0.73         6
          ovos-skill-diagnostics.openvoiceos:query_memory_usage.intent       1.00      1.00      1.00         2
         ovos-skill-diagnostics.openvoiceos:query_ovos_location.intent       0.00      0.00      0.00         1
          ovos-skill-diagnostics.openvoiceos:query_primary_lang.intent       1.00      1.00      1.00         9
             ovos-skill-diagnostics.openvoiceos:query_user_lang.intent       1.00      1.00      1.00         2
         ovos-skill-diagnostics.openvoiceos:query_user_location.intent       1.00      1.00      1.00         1
                   ovos-skill-hello-world.openvoiceos:Greetings.intent       0.00      0.00      0.00         2
                    ovos-skill-icanhazdadjokes.openvoiceos:joke.intent       0.75      1.00      0.86         3
             ovos-skill-icanhazdadjokes.openvoiceos:search_joke.intent       1.00      1.00      1.00         2
                            ovos-skill-ip.openvoiceos:what.ssid.intent       1.00      1.00      1.00         5
                      ovos-skill-iss-location.openvoiceos:WhoISSIntent       1.00      1.00      1.00         1
                      ovos-skill-iss-location.openvoiceos:about.intent       1.00      1.00      1.00         4
                   ovos-skill-iss-location.openvoiceos:when_iss.intent       1.00      1.00      1.00         1
                  ovos-skill-iss-location.openvoiceos:where_iss.intent       1.00      1.00      1.00         2
                             ovos-skill-laugh.openvoiceos:Laugh.intent       0.67      1.00      0.80         2
                       ovos-skill-laugh.openvoiceos:RandomLaugh.intent       1.00      1.00      1.00         2
          ovos-skill-moviemaster.openvoiceos:genre.movie.search.intent       1.00      1.00      1.00         4
             ovos-skill-moviemaster.openvoiceos:genre.tv.search.intent       1.00      1.00      1.00         7
                  ovos-skill-moviemaster.openvoiceos:movie.cast.intent       1.00      1.00      1.00         2
           ovos-skill-moviemaster.openvoiceos:movie.description.intent       1.00      1.00      1.00         8
                ovos-skill-moviemaster.openvoiceos:movie.genres.intent       1.00      1.00      1.00         4
           ovos-skill-moviemaster.openvoiceos:movie.information.intent       1.00      1.00      1.00        11
               ovos-skill-moviemaster.openvoiceos:movie.popular.intent       1.00      1.00      1.00         4
            ovos-skill-moviemaster.openvoiceos:movie.production.intent       1.00      1.00      1.00         1
       ovos-skill-moviemaster.openvoiceos:movie.recommendations.intent       1.00      1.00      1.00        25
               ovos-skill-moviemaster.openvoiceos:movie.runtime.intent       1.00      1.00      1.00        19
                   ovos-skill-moviemaster.openvoiceos:movie.top.intent       1.00      1.00      1.00        67
                  ovos-skill-moviemaster.openvoiceos:movie.year.intent       1.00      1.00      1.00         8
                        ovos-skill-news.openvoiceos:global_news.intent       1.00      0.89      0.94         9
                               ovos-skill-news.openvoiceos:news.intent       0.89      1.00      0.94        16
                     ovos-skill-personal.openvoiceos:WhatAreYou.intent       1.00      1.00      1.00         1
                ovos-skill-personal.openvoiceos:WhenWereYouBorn.intent       1.00      1.00      1.00         2
               ovos-skill-personal.openvoiceos:WhereWereYouBorn.intent       1.00      1.00      1.00         2
                      ovos-skill-personal.openvoiceos:WhoAreYou.intent       1.00      1.00      1.00         1
                     ovos-skill-personal.openvoiceos:WhoMadeYou.intent       1.00      1.00      1.00         2
                   ovos-skill-volume.openvoiceos:volume.default.intent       1.00      1.00      1.00         1
                      ovos-skill-volume.openvoiceos:volume.high.intent       1.00      1.00      1.00         1
                       ovos-skill-volume.openvoiceos:volume.low.intent       1.00      1.00      1.00         1
                       ovos-skill-volume.openvoiceos:volume.max.intent       1.00      1.00      1.00         1
                      ovos-skill-volume.openvoiceos:volume.mute.intent       0.00      0.00      0.00         1
                    ovos-skill-volume.openvoiceos:volume.unmute.intent       0.00      0.00      0.00         1
                         ovos-skill-weather.openvoiceos:is_rain.intent       1.00      1.00      1.00         1
                         ovos-skill-wikihow.openvoiceos:wikihow.intent       1.00      1.00      1.00         5
                          ovos-skill-wikipedia.openvoiceos:wiki.intent       1.00      1.00      1.00         3
                  ovos-skill-wikipedia.openvoiceos:wikiroulette.intent       1.00      1.00      1.00         3
                      ovos-skill-wordnet.openvoiceos:definition.intent       0.00      0.00      0.00         1

                                                              accuracy                           0.97       427
                                                             macro avg       0.88      0.89      0.88       427
                                                          weighted avg       0.97      0.97      0.97       427

```

