# Model Evaluation Metrics Summary
## catalan - Model: Jarbas/m2v-256-roberta-base-ca-cased-sts
### Accuracy: 0.997996744710154
### F1 Score: 0.997679199882446
### Cohen Kappa Score: 0.9975525183347579
### Matthews Corrcoef Score: 0.997552880123391
### Classification Report:
```
                                                                        precision    recall  f1-score   support

                                             common_query:common_query       1.00      0.91      0.95        11
                         ovos-skill-alerts.openvoiceos:AddListSubitems       1.00      1.00      1.00         2
                             ovos-skill-alerts.openvoiceos:CancelAlert       0.00      0.00      0.00         1
                             ovos-skill-alerts.openvoiceos:CreateAlarm       1.00      1.00      1.00         2
                              ovos-skill-alerts.openvoiceos:CreateList       1.00      1.00      1.00         1
                          ovos-skill-alerts.openvoiceos:CreateReminder       1.00      1.00      1.00         1
                       ovos-skill-alerts.openvoiceos:DeleteListEntries       1.00      1.00      1.00         1
                       ovos-skill-alerts.openvoiceos:DeleteTodoEntries       0.00      0.00      0.00         1
                              ovos-skill-alerts.openvoiceos:ListAlerts       1.00      1.00      1.00         2
                    ovos-skill-alerts.openvoiceos:missed_alerts.intent       1.00      1.00      1.00       902
         ovos-skill-audio-recording.openvoiceos:start_recording.intent       1.00      1.00      1.00        57
             ovos-skill-boot-finished.openvoiceos:are_you_ready.intent       1.00      1.00      1.00        33
ovos-skill-boot-finished.openvoiceos:disable_ready_notification.intent       1.00      1.00      1.00      2048
 ovos-skill-boot-finished.openvoiceos:enable_ready_notification.intent       1.00      1.00      1.00      2458
                      ovos-skill-camera.openvoiceos:have_camera.intent       1.00      1.00      1.00         1
                    ovos-skill-confucius-quotes.openvoiceos:who.intent       1.00      1.00      1.00         1
           ovos-skill-date-time.openvoiceos:date.future.weekend.intent       1.00      1.00      1.00       117
             ovos-skill-date-time.openvoiceos:date.last.weekend.intent       1.00      1.00      1.00       519
              ovos-skill-date-time.openvoiceos:weekday.for.date.intent       1.00      1.00      1.00         2
                ovos-skill-date-time.openvoiceos:what.day.is.it.intent       1.00      1.00      1.00         7
              ovos-skill-date-time.openvoiceos:what.month.is.it.intent       1.00      1.00      1.00         5
               ovos-skill-date-time.openvoiceos:what.time.is.it.intent       0.99      1.00      0.99        92
          ovos-skill-date-time.openvoiceos:what.time.will.it.be.intent       1.00      1.00      1.00       277
            ovos-skill-date-time.openvoiceos:what.weekday.is.it.intent       1.00      1.00      1.00         5
               ovos-skill-date-time.openvoiceos:what.year.is.it.intent       1.00      1.00      1.00         3
       ovos-skill-days-in-history.openvoiceos:births_in_history.intent       0.50      1.00      0.67         1
       ovos-skill-days-in-history.openvoiceos:deaths_in_history.intent       0.00      0.00      0.00         1
        ovos-skill-days-in-history.openvoiceos:today_in_history.intent       1.00      1.00      1.00       217
                         ovos-skill-ddg.openvoiceos:search_duck.intent       1.00      1.00      1.00        21
             ovos-skill-diagnostics.openvoiceos:query_cpu_usage.intent       1.00      1.00      1.00        12
           ovos-skill-diagnostics.openvoiceos:query_extra_langs.intent       0.97      0.94      0.96        34
                   ovos-skill-diagnostics.openvoiceos:query_gpu.intent       1.00      1.00      1.00         5
        ovos-skill-diagnostics.openvoiceos:query_kernel_version.intent       1.00      1.00      1.00         7
                 ovos-skill-diagnostics.openvoiceos:query_langs.intent       0.99      0.99      0.99       145
          ovos-skill-diagnostics.openvoiceos:query_memory_usage.intent       1.00      1.00      1.00        10
         ovos-skill-diagnostics.openvoiceos:query_ovos_location.intent       0.97      1.00      0.99        36
          ovos-skill-diagnostics.openvoiceos:query_primary_lang.intent       1.00      1.00      1.00        71
             ovos-skill-diagnostics.openvoiceos:query_user_lang.intent       1.00      1.00      1.00        26
         ovos-skill-diagnostics.openvoiceos:query_user_location.intent       1.00      0.95      0.97        19
               ovos-skill-dictation.openvoiceos:start_dictation.intent       1.00      1.00      1.00        93
                ovos-skill-dictation.openvoiceos:stop_dictation.intent       1.00      1.00      1.00        25
             ovos-skill-fuster-quotes.openvoiceos:fuster_quotes.intent       1.00      1.00      1.00         5
                       ovos-skill-fuster-quotes.openvoiceos:who.intent       1.00      1.00      1.00         2
                   ovos-skill-hello-world.openvoiceos:Greetings.intent       1.00      0.40      0.57         5
                    ovos-skill-icanhazdadjokes.openvoiceos:joke.intent       1.00      1.00      1.00         7
             ovos-skill-icanhazdadjokes.openvoiceos:search_joke.intent       1.00      1.00      1.00        15
                            ovos-skill-ip.openvoiceos:what.ssid.intent       1.00      1.00      1.00         2
                      ovos-skill-iss-location.openvoiceos:WhoISSIntent       1.00      1.00      1.00         1
                      ovos-skill-iss-location.openvoiceos:about.intent       0.97      1.00      0.99        38
                   ovos-skill-iss-location.openvoiceos:when_iss.intent       1.00      1.00      1.00       205
                  ovos-skill-iss-location.openvoiceos:where_iss.intent       1.00      1.00      1.00        53
                             ovos-skill-laugh.openvoiceos:Laugh.intent       1.00      1.00      1.00         7
                       ovos-skill-laugh.openvoiceos:RandomLaugh.intent       1.00      1.00      1.00         5
                           ovos-skill-laugh.openvoiceos:haunted.intent       1.00      1.00      1.00         2
                         ovos-skill-naptime.openvoiceos:naptime.intent       1.00      0.83      0.91         6
                        ovos-skill-news.openvoiceos:global_news.intent       1.00      1.00      1.00        11
                               ovos-skill-news.openvoiceos:news.intent       1.00      1.00      1.00        77
                  ovos-skill-parrot.openvoiceos:did.you.hear.me.intent       1.00      0.50      0.67         2
                       ovos-skill-parrot.openvoiceos:repeat.stt.intent       1.00      1.00      1.00         2
                       ovos-skill-parrot.openvoiceos:repeat.tts.intent       1.00      1.00      1.00         6
                            ovos-skill-parrot.openvoiceos:speak.intent       1.00      1.00      1.00         2
                     ovos-skill-parrot.openvoiceos:start_parrot.intent       0.80      0.80      0.80         5
                      ovos-skill-parrot.openvoiceos:stop_parrot.intent       0.92      1.00      0.96        11
                     ovos-skill-personal.openvoiceos:WhatAreYou.intent       1.00      1.00      1.00         3
                ovos-skill-personal.openvoiceos:WhenWereYouBorn.intent       1.00      1.00      1.00         4
               ovos-skill-personal.openvoiceos:WhereWereYouBorn.intent       1.00      1.00      1.00         5
                      ovos-skill-personal.openvoiceos:WhoAreYou.intent       0.00      0.00      0.00         1
                     ovos-skill-personal.openvoiceos:WhoMadeYou.intent       1.00      1.00      1.00         7
                   ovos-skill-volume.openvoiceos:volume.default.intent       1.00      1.00      1.00         4
                      ovos-skill-volume.openvoiceos:volume.high.intent       1.00      1.00      1.00         1
                       ovos-skill-volume.openvoiceos:volume.low.intent       1.00      1.00      1.00         1
                       ovos-skill-volume.openvoiceos:volume.max.intent       1.00      1.00      1.00         2
                      ovos-skill-volume.openvoiceos:volume.mute.intent       1.00      1.00      1.00         1
               ovos-skill-volume.openvoiceos:volume.mute.toggle.intent       1.00      1.00      1.00         1
                    ovos-skill-volume.openvoiceos:volume.unmute.intent       0.00      0.00      0.00         1
                         ovos-skill-weather.openvoiceos:is_rain.intent       1.00      1.00      1.00        19
                         ovos-skill-wikihow.openvoiceos:wikihow.intent       1.00      1.00      1.00        20
                          ovos-skill-wikipedia.openvoiceos:wiki.intent       1.00      1.00      1.00        27
                  ovos-skill-wikipedia.openvoiceos:wikiroulette.intent       1.00      1.00      1.00        15
                    ovos-skill-wolfie.openvoiceos:search_wolfie.intent       1.00      1.00      1.00         8
                         ovos-skill-wordnet.openvoiceos:antonym.intent       1.00      1.00      1.00        11
                      ovos-skill-wordnet.openvoiceos:definition.intent       0.50      1.00      0.67         1
                         ovos-skill-wordnet.openvoiceos:holonym.intent       1.00      1.00      1.00        11
                        ovos-skill-wordnet.openvoiceos:hypernym.intent       1.00      1.00      1.00        26
                         ovos-skill-wordnet.openvoiceos:hyponym.intent       1.00      1.00      1.00        59
                           ovos-skill-wordnet.openvoiceos:lemma.intent       1.00      1.00      1.00         7
                  ovos-skill-wordnet.openvoiceos:search_wordnet.intent       1.00      1.00      1.00        11

                                                              accuracy                           1.00      7987
                                                             macro avg       0.93      0.92      0.92      7987
                                                          weighted avg       1.00      1.00      1.00      7987

```

