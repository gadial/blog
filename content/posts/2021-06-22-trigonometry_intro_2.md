---
title: "מה בעצם הולך בטריגונומטריה בתיכון? (חלק ב')"
layout: post
categories:
  - כללי
tags:
  - טריגונומטריה
---


<h2>מבוא</h2>

בפוסט הקודם שלי על טריגונומטריה הצגתי את הפונקציות {% equation %}\sin,\cos{% endequation %} ונתתי הגדרה שלהן לכל זווית אפשרית. הרעיון הבסיסי היה שהן מספרות לנו מה הקואורדינטות של נקודה שנמצאת על מעגל היחידה שאליה מגיעים על ידי כך שמתחילים עם רדיוס שנח במאוזן על הכיוון החיובי של ציר {% equation %}x{% endequation %}, ומתחילים לסובב אותו ורואים עד לאן מגיעים.

הגדרה זה טוב ויפה, אבל בסופו של דבר המטרה שלי היא להבין איך פותרים תרגילים בטריגונומטריה, ולצורך כך צריך קודם כל להבין את דף הנוסחאות המזעזע שפתחתי איתו את הפוסט הקודם:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigo_formulas.png" alt=""/>

מה שיעניין אותי עכשיו הוא הנוסחאות

<ul> <li>{% equation %}\sin\left(\alpha\pm\beta\right)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta{% endequation %}</li>


<li>{% equation %}\cos\left(\alpha\pm\beta\right)=\cos\alpha\cos\beta\mp\cos\alpha\cos\beta{% endequation %}</li>

</ul>

מה הנוסחאות הללו אומרות? איך מגיעים אליהן? מהשאלות הללו אני רוצה להתחיל, אבל כאן אני נקלע לדיסוננס חריף מאוד בין גדי תלמיד התיכון ובין גדי שלמד באוניברסיטה. גדי של התיכון מכיר סינוסים וקוסינוסים רק מנקודת המבט <strong>הגאומטרית</strong> שהצגתי בפוסט הקודם. מנקודת המבט הזו, לא יעזור כלום - ההוכחה של הנוסחאות הללו היא <strong>קשה יחסית</strong> (למרות שנעשה אותה פה באופן מלא; היא רחוקה מלהיות סוף העולם) וקשה לקבל ממנה אינטואיציה או לזכור את הנוסחאות. אבל באוניברסיטה רואים דרך <strong>שונה לגמרי</strong> להגיע אל הנוסחאות הללו; דרך שהיא הרבה יותר פשוטה, והופכת את הנוסחאות כמעט לטריוויאליות לשינון. המחיר הוא שהדרך הזו מתבססת על הגדרה מסויימת שאני בהחלט הולך לתת בפוסט הזה, אבל בלי רקע מתמטי מתאים עשויה להיראות כמו <strong>רמאות גמורה</strong>. אז ברשותכם, אני אתחיל עם הגאומטריה דווקא, ואז אגיע אל הדרך האחרת.

בדרך הגאומטרית אני אצטרך להוכיח רק אחת מארבע הנוסחאות, את {% equation %}\sin\left(\alpha+\beta\right)=\sin\alpha\cos\beta+\cos\alpha\sin\beta{% endequation %}; אחר כך אני אראה איך מהנוסחה הזו אפשר לקבל יחסית בקלות את היתר.

<h2>הוכחה גאומטרית</h2>

נתחיל, אם כן, עם משולש:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigsum1.png" alt=""/>

המשולש {% equation %}OAB{% endequation %} הוא ישר זווית (ספציפית, {% equation %}\angle OBA=90^{\circ}{% endequation %}). השימוש ב-{% equation %}O{% endequation %} בתור אחד הקודקודים בא לרמז שאני מצייר את המשולש הזה על <strong>מעגל היחידה</strong> ש-{% equation %}O{% endequation %} הוא המרכז שלו, ו-{% equation %}A{% endequation %} היא הנקודה שעל המעגל עצמו; {% equation %}OA{% endequation %} הוא <strong>היתר </strong>של המשולש ומכיוון שאני מתבסס על מעגל היחידה אני מניח ש-{% equation %}\left|OA\right|=1{% endequation %}. בהינתן אלו, {% equation %}\sin\left(\alpha+\beta\right)=\left|AB\right|{% endequation %}, כך שצריך לחשב את אורך הצלע {% equation %}AB{% endequation %}. לשם כך אני אעזר בקו שפיצל את הזווית במשולש לסכום {% equation %}\alpha+\beta{% endequation %}. הרעיון הוא לקחת את הקו הזה ו<strong>להמשיך</strong> אותו גם מעבר למשולש, עד שהוא יהיה ארוך מספיק כדי שאוכל להוריד אליו <strong>אנך</strong> מנקודה {% equation %}A{% endequation %}. ככה זה נראה:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigsum2.png" alt=""/>

המשמעות של "אנך" היא שהקו {% equation %}AQ{% endequation %} שיורד אל {% equation %}OQ{% endequation %} פוגש אותו בזווית של 90 מעלות, כלומר {% equation %}\angle OQA=90^{\circ}{% endequation %}. התעלול הזה של "להוריד אנך מנקודה לקו קיים" הוא אחד מהשימושיים ביותר כשפותרים תרגילים בגאומטריה כי אנכים עושים כל מני דברים נחמדים. כמובן, אפשר לשאול ובצד <strong>איך</strong> בכלל אפשר להוריד אנך. אני סתם ציירתי קו מ-{% equation %}A{% endequation %} שנראה לי בערך מאונך (ואז כשניסיתי לצייר את הריבוע הקטן של הזווית הישרה ראיתי שיצא לי עקום לגמרי ותיקנתי) אבל כבר אוקלידס עסק בפתרון פורמלי יותר לשאלה הזו. ב"יסודות" של אוקלידס, בטענה 11, מגיע הסבר איך ליצור אנך כזה - הרעיון הוא להשתמש ב<strong>מחוגה</strong>, אחד משני כלי העבודה הבסיסיים שאוקלידס עובד איתם (השני הוא סרגל לא מסומן). כשהייתי בתיכון השימוש היחיד למחוגה אצלי היה לזנק מן הקלמר ולפצוע אותי באצבע - באמת, הייתה לי טראומה מהמכשיר הזה.

בואו נסתכל לרגע על המשולש {% equation %}OQA{% endequation %} שקיבלנו. זה משולש ישר זווית, והיתר שלו הוא {% equation %}AO{% endequation %} שכבר אמרתי שאני אוהב כי {% equation %}\left|AO\right|=1{% endequation %}. במילים אחרות, אחרי שהתחלנו עם משולש ישר זווית ש-{% equation %}AO{% endequation %} הייתה היתר שלו, עכשיו בנינו <strong>עוד</strong> משולש ישר זווית ש-{% equation %}AO{% endequation %} היא היתר שלו, אבל הזוויות שלו שונות: במקום שתהיה בו הזווית {% equation %}\alpha+\beta{% endequation %} יש בו את הזווית {% equation %}\beta{% endequation %} לבדה. בפרט, {% equation %}\left|AQ\right|=\sin\beta{% endequation %} ו-{% equation %}\left|OQ\right|=\cos\beta{% endequation %}. זה מקדם אותנו משמעותית - אורכי שתי הצלעות הללו הן חצי מ"נתוני הבסיס" שאנחנו מצפים לקבל את התוצאה שלנו באמצעותם. רק צריך איכשהו להכניס את {% equation %}\alpha{% endequation %} לתמונה גם כן.

העניין הוא ש-{% equation %}\alpha{% endequation %} כבר בתמונה ופשוט לא שמנו לב. בואו נסתכל לרגע על הנקודה שבה נחתכים {% equation %}AB{% endequation %} ו-{% equation %}OQ{% endequation %}, שלא נתתי לה שם כדי לא לסרבל יותר מדי:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigsum3.png" alt=""/>

סביב הנקודה הזו יש ארבע זוויות שסימנתי ב-1,2,3,4. כל צמד זוויות שלא נוגעות זו בזו נקראות <strong>זוויות קודקודיות</strong> (כי יש להן רק קודקוד משותף). כאן 1 ו-3 הן הזוויות הקודקודיות שיעניינו אותי. מה שיפה בזוויות קודקודיות הוא שהן תמיד שוות זו לזו. כדי לראות את זה, שימו לב שהזוויות 1 ו-2 משלימות ביחד חצי סיבוב בדיוק, על הצד השמאלי של הישר {% equation %}AB{% endequation %}. כלומר, אם אני מסמן אותן בתור {% equation %}\gamma_{1},\gamma_{2}{% endequation %} אז {% equation %}\gamma_{1}+\gamma_{2}=180^{\circ}{% endequation %} כי חצי סיבוב הוא בדיוק 180 מעלות. עכשיו, גם הזוויות 2,3 משלימות חצי סיבוב בדיוק, על הצד העליון של {% equation %}OQ{% endequation %} ולכן {% equation %}\gamma_{3}+\gamma_{2}=180^{\circ}=\gamma_{1}+\gamma_{2}{% endequation %} ואחרי חיסור {% equation %}\alpha_{2}{% endequation %} משני האגפים נקבל {% equation %}\gamma_{1}=\gamma_{3}{% endequation %}. אין כאן קסם שייחודי לבניה הספציפית הזו; זו תוצאה כללית בגאומטריה.

עכשיו, הזווית {% equation %}\gamma_{1}{% endequation %} הזו משתתפת במשולש התחתון יחד עם הזווית הישרה {% equation %}\angle ABO{% endequation %} והזווית {% equation %}\angle BOQ{% endequation %} ששווה ל-{% equation %}\alpha{% endequation %} המקורי שלנו. המסקנה היא ש-{% equation %}\gamma_{1}=90^{\circ}-\alpha{% endequation %} (כי סכום הזוויות במשולש הוא {% equation %}180^{\circ}{% endequation %}). לכן גם {% equation %}\gamma_{3}{% endequation %} שווה ואז נקבל שהזווית {% equation %}\angle BAQ{% endequation %} העליונה שווה גם ל-{% equation %}\alpha{% endequation %} שזה בעצם מה שרציתי להראות בכל הטררם הנוכחי.

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigsum4.png" alt=""/>

אנחנו די קרובים לסיום למרות שזה עדיין ממש לא נראה כך - עדיין נדרשות ממני כמה בניות עזר. נתחיל עם {% equation %}OQ{% endequation %}. כבר חישבנו קודם ש-{% equation %}\left|OQ\right|=\cos\beta{% endequation %}, ועכשיו אני רוצה לנצל את זה. לצורך כך בואו נשים לב לכך שאם רק נוריד אנך מ-{% equation %}Q{% endequation %} אל ההמשך של הישר שעובר דרך {% equation %}OB{% endequation %} נקבל משולש ישר זווית ש-{% equation %}OQ{% endequation %} הוא היתר שלו:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigsum5.png" alt=""/>

במשולש החדש הזה מתקיים {% equation %}\frac{\left|RQ\right|}{\left|OQ\right|}=\sin\alpha{% endequation %} פשוט על פי הגדרת סינוס. לכן, אם נשתמש ב-{% equation %}\left|OQ\right|=\cos\beta{% endequation %}, נקבל {% equation %}\left|RQ\right|=\sin\alpha\cos\beta{% endequation %}. הופה! זה דבר רציני ביותר - קיבלנו כבר את אחד משני הביטויים שמשתתפים בסכום הסופי, והבנו מאיפה צצה המכפלה הזו של סינוס של זווית אחת בקוסינוס של הזווית השניה. אבל איך אפשר לקשר את {% equation %}RQ{% endequation %} הזה שהוא קטע חדש שהוספנו משום מקום, אל מה שאנחנו רוצים לחשב, שהוא כזכור האורך של {% equation %}AB{% endequation %}? ובכן, אפשר להיעזר בכך שגם {% equation %}AB{% endequation %} וגם {% equation %}RQ{% endequation %} שניהם <strong>מאונכים</strong> מ-{% equation %}OR{% endequation %} כדי לבנות <strong>מלבן</strong> שמערב אותם:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigsum6.png" alt=""/>

במלבן {% equation %}PQRB{% endequation %}, שהתקבל על ידי הורדת אנך מ-{% equation %}Q{% endequation %} אל {% equation %}AB{% endequation %}, אנחנו יודעים שהצלע {% equation %}QR{% endequation %} שווה באורכה לצלע {% equation %}PB{% endequation %}, כלומר {% equation %}\left|PB\right|=\sin\alpha\cos\beta{% endequation %}. כדי לסיים את ההוכחה צריך לחשב את האורך של {% equation %}AP{% endequation %}, כי {% equation %}\left|AB\right|=\left|AP\right|+\left|PB\right|{% endequation %}. למרבה המזל, זה חישוב קל במיוחד: המשולש {% equation %}APQ{% endequation %} הוא ישר זווית עם יתר {% equation %}AQ{% endequation %} וכבר חישבנו ומצאנו שהזווית {% equation %}\angle PAQ{% endequation %} היא {% equation %}\alpha{% endequation %}, ולכן {% equation %}\frac{\left|AP\right|}{\left|AQ\right|}=\cos\alpha{% endequation %}. ראינו קודם ש-{% equation %}\left|AQ\right|=\sin\beta{% endequation %}, ולכן נקבל ש-{% equation %}\left|AP\right|=\cos\alpha\sin\beta{% endequation %}. בזאת סיימנו:

{% equation %}\left|AB\right|=\left|AP\right|+\left|PB\right|=\sin\alpha\cos\beta+\cos\alpha\sin\beta{% endequation %}

יפה מאוד! האם אפשר לנוח כעת על זרי הדפנה? ובכן, לא.

<h2>מה יצא לנו מההוכחה הגאומטרית?</h2>

למה עוד לא סיימנו? ראשית, הבטחתי דרך טובה יותר לזכור את הנוסחה הזו מאשר שינון ההוכחה הזו, שאמנם התחלתי לחבב תוך כדי כתיבת הפוסט אבל היא עדיין לא בדיוק משהו שקל לזכור. אבל שנית, וחמור יותר, ההוכחה הזו התבססה על <strong>משולשים</strong>, כלומר הניחה במובלע שהזוויות {% equation %}\alpha,\beta{% endequation %} גם יחד הן קטנות מספיק - סכומן לא עולה על 90 מעלות. העניין הוא שראינו בפוסט הקודם שסינוס וקוסינוס הם בעצם רק מה שקורה בטווח המעלות הזה; כל מה שקורה מחוץ לטווח המעלות מתקבל בצורה כלשהי מהפונקציה בתוך טווח המעלות הזה (אולי עם שיקוף כלשהו). לכן אני אוותר על החלוקה למקרים הפדנטית שנדרשת כדי להוכיח שאפשר להיעזר בתוצאה הזו כדי להוכיח את התוצאה הכללית ביותר.

בכל זאת, אי אפשר בלי דוגמא כלשהי כדי שנשתכנע שאין פה רמאות גמורה. בואו נניח אם כן ש-{% equation %}\alpha,\beta{% endequation %} הן זוויות בטווח הנכון של בין {% equation %}0^{\circ}{% endequation %} ל-{% equation %}90^{\circ}{% endequation %} אבל <strong>הסכום</strong> שלהן גדול מ-{% equation %}90^{\circ}{% endequation %}, כלומר {% equation %}90^{\circ}\le\alpha+\beta\le180^{\circ}{% endequation %}. כעת, נזכור שראינו בפוסט הקודם ש-

{% equation %}\sin\left(180^{\circ}-\gamma\right)=\sin\gamma{% endequation %}

כלומר, במקרה שלנו:

{% equation %}\sin\left(\alpha+\beta\right)=\sin\left(180^{\circ}-\left(\alpha+\beta\right)\right)=\sin\left(\left(90^{\circ}-\alpha\right)+\left(90^{\circ}-\beta\right)\right){% endequation %}

עכשיו, {% equation %}\left(90^{\circ}-\alpha\right){% endequation %} ו-{% equation %}\left(90^{\circ}-\beta\right){% endequation %} הן שתיהן זוויות ש:

<ul> <li>נמצאות בטווח שבין {% equation %}0^{\circ}{% endequation %} ובין {% equation %}90^{\circ}{% endequation %}</li>


<li>סכומן לא עולה על {% equation %}90^{\circ}{% endequation %} (כי סכומן הוא {% equation %}180^{\circ}-\left(\alpha+\beta\right){% endequation %} שהוא קטן מ-{% equation %}90^{\circ}{% endequation %} כי {% equation %}\left(\alpha+\beta\right){% endequation %} גדול מ-{% equation %}90^{\circ}{% endequation %})</li>

</ul>

לכן התוצאה שהוכחנו זה עתה עובדת עבור הזוויות הללו, ונקבל:

{% equation %}\sin\left(\alpha+\beta\right)=\sin\left(90^{\circ}-\alpha\right)\cos\left(90^{\circ}-\beta\right)+\sin\left(90^{\circ}-\beta\right)\cos\left(90^{\circ}-\alpha\right){% endequation %}

כזכור מהפוסט הקודם, {% equation %}\sin\left(90^{\circ}-\alpha\right)=\cos\alpha{% endequation %} ו-{% equation %}\cos\left(90^{\circ}-\alpha\right)=\sin\alpha{% endequation %}, כלומר אגף ימין של המשוואה שלעיל הופך להיות

{% equation %}\cos\alpha\sin\beta+\sin\alpha\cos\beta{% endequation %}

וזה מה שאנחנו רוצים, באופן לא מפתיע. כך זה יעבוד גם בכל מקרה אחר - כאמור, לא אכנס לפרטים הללו.

מה שכן כדאי להרחיב עליו הוא איך מהנוסחה שכבר מצאתי אני מגיע לכל היתר. כזכור, התחלתי עם הנוסחאות הבאות:

<ul> <li>{% equation %}\sin\left(\alpha\pm\beta\right)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta{% endequation %}</li>


<li>{% equation %}\cos\left(\alpha\pm\beta\right)=\cos\alpha\cos\beta\mp\cos\alpha\cos\beta{% endequation %}</li>

</ul>

אלו ארבע נוסחאות שונות, אבל הוכחתי רק אחת מהן - את {% equation %}\sin\left(\alpha+\beta\right)=\sin\alpha\cos\beta+\cos\alpha\sin\beta{% endequation %}. לכל היתר אפשר להגיע בקלות בעזרתה אם ניעזר בנוסחאות אחרות שכבר ראינו.

נתחיל עם {% equation %}\sin\left(\alpha-\beta\right){% endequation %}. בעצם, יש לנו כאן חיבור בתחפושת: {% equation %}\sin\left(\alpha-\beta\right)=\sin\left(\alpha+\left(-\beta\right)\right){% endequation %}. כלומר, אם כבר הסכמנו שנוסחת החיבור עובדת <strong>לכל</strong> זווית, אז היא עובדת גם עבור מינוס של זוויות (מינוס של מספר הוא... מספר). כלומר, אנחנו מקבלים:

{% equation %}\sin\left(\alpha-\beta\right)=\sin\left(\alpha+\left(-\beta\right)\right)=\sin\alpha\cos\left(-\beta\right)+\cos\alpha\sin\left(-\beta\right){% endequation %}

עכשיו בואו ניזכר איך סינוס וקוסינוס מתמודדים עם מינוס של זווית: לקוסינוס לא אכפת, אבל סינוס מוכפל במינוס:

{% equation %}\sin\left(-\beta\right)=-\sin\beta{% endequation %}

{% equation %}\cos\left(-\beta\right)=\cos\beta{% endequation %}

ולכן נקבל:

{% equation %}\sin\alpha\cos\left(-\beta\right)+\cos\alpha\sin\left(-\beta\right)=\sin\alpha\cos\beta-\cos\alpha\sin\beta{% endequation %}

וזו בדיוק הנוסחה השניה שרצינו.

נעבור עכשיו אל נוסחת הסכום עבור קוסינוס. נתחיל עם תזכורת על האופן שבו סינוס וקוסינוס מחוברים יחד:

{% equation %}\sin\left(\alpha\right)=\cos\left(90^{\circ}-\alpha\right){% endequation %}

{% equation %}\cos\left(\alpha\right)=\sin\left(90^{\circ}-\alpha\right){% endequation %}

בואו נשתמש בזה כדי לחשב את {% equation %}\cos\left(\alpha+\beta\right){% endequation %}:

{% equation %}\cos\left(\alpha+\beta\right)=\sin\left(90^{\circ}-\left(\alpha+\beta\right)\right)=\sin\left(\left(90^{\circ}-\alpha\right)-\beta\right){% endequation %}

כלומר, עברתי לסינוס של הפרש שתי זוויות: אחת היא {% equation %}90^{\circ}-\alpha{% endequation %} והשניה היא {% equation %}\beta{% endequation %}. על זה אפשר להשתמש בנוסחת ההפרש שראינו קודם:

{% equation %}\sin\left(\left(90^{\circ}-\alpha\right)-\beta\right)=\sin\left(90^{\circ}-\alpha\right)\cos\beta-\cos\left(90^{\circ}-\alpha\right)\sin\beta{% endequation %}

ולסיום, אפשר להעלים את ה-90 מעלות על ידי מעבר מסינוס לקוסינוס וההפך:

{% equation %}\sin\left(90^{\circ}-\alpha\right)\cos\beta-\cos\left(90^{\circ}-\alpha\right)\sin\beta=\cos\alpha\cos\beta-\sin\alpha\sin\beta{% endequation %}

וזו בדיוק הנוסחה שרצינו. עבור הפרש קוסינוסים עושים את אותו תעלול של החלפת {% equation %}\beta{% endequation %} ב-{% equation %}-\beta{% endequation %} שעשינו קודם ומקבלים שהמקדם של {% equation %}\sin\alpha\sin\beta{% endequation %} יהפוך לפלוס. זה מסיים את הוכחת ארבע הנוסחאות; כפי שאנחנו רואים, עיקר העבודה הייתה להוכיח את נוסחת החיבור עבור סינוס.

ועכשיו הבה ונעבור למשהו שונה לגמרי.

<h2>נוסחת אוילר</h2>

אני חושב שהדבר הכי פשוט לעשות עם נוסחת אוילר הוא פשוט להציג אותה ואז להסביר מה הולך פה. אז הנה היא:

{% equation %}e^{i\alpha}=\cos\alpha+i\sin\alpha{% endequation %}

מה יש לנו בנוסחה הזו? ובכן, באגף ימין יש לנו את {% equation %}\sin\alpha{% endequation %} ואת {% equation %}\cos\alpha{% endequation %} שאנחנו כבר מכירים. פרט אליהם יש את האות {% equation %}i{% endequation %}. מה האות הזו מייצגת כאן? היא מייצגת מספר שמקיים את התכונה {% equation %}i^{2}=-1{% endequation %}. מספר כזה הוא דוגמא למה שנקרא <strong>מספר מרוכב</strong> ובהחלט ייתכן שחלק מהקוראים לא מכירים; אבל גם לא צריך להכיר אותו כאן מעבר ל"זה מספר שמקיים {% equation %}i^{2}=-1{% endequation %} והוא ממש ממש אמיתי ולא סתם איזה שקר שהמצאנו כרגע בבקשה תאמינו לנו" (ולמה בכלל שזה ירגיש כמו שקר? ובכן, כי כל מספר ממשי {% equation %}a{% endequation %} מקיים {% equation %}a^{2}\ge0{% endequation %} ובפרט אי אפשר לקבל {% equation %}-1{% endequation %} על ידי העלאה בריבוע של מספר ממשי).

באגף שמאל יש לנו את אותו {% equation %}i{% endequation %} ואת הזווית {% equation %}\alpha{% endequation %} כשהם נמצאים במעריך של חזקה שהבסיס שלה מסומן ב-{% equation %}e{% endequation %}. מי זה {% equation %}e{% endequation %}? ובכן, זה לא מספר אקראי; זה מספר חשוב במתמטיקה שהוא בערך {% equation %}2.71828\ldots{% endequation %}. אבל כמו עם {% equation %}i{% endequation %}, כך גם כאן; כדי להיעזר בנוסחת אוילר לא צריך לדעת עליו שום דבר מעבר לכך.

בנוסף לכך, כדי שהנוסחה "תעבוד" צריך ש-{% equation %}\alpha{% endequation %} תהיה נתונה לא במעלות אלא במשהו שנקרא <strong>רדיאנים</strong>, אבל כמו שכבר אמרתי - גם על רדיאנים לא צריך לדעת שום דבר אם אנחנו רק רוצים להיעזר בנוסחת אוילר.

אז הנה שתי שאלות שאני הולך לענות עליהן:

<ol> <li><strong>איך</strong> נעזרים בנוסחת אוילר בשביל לקבל את נוסחת הסכום?</li>


<li><strong>למה</strong> נוסחת אוילר נכונה בכלל?</li>

</ol>

אני מתחיל עם שאלה 1 כי התשובה ל-2 מאוד מסובכת ו<strong>לא הכרחית</strong> כל עוד סומכים עלי בעיניים עצומות. בשביל 1, צריך להיזכר לרגע איך עובדים חוקי החזקות הרגילים:

{% equation %}a^{x}\cdot a^{y}=a^{x+y}{% endequation %}

במילים אחרות - אם כופלים שתי חזקות עם אותו בסיס, מקבלים חזקה עם הבסיס הזה, שהמעריך שלה הוא <strong>סכום</strong> המעריכים של החזקות. חזקה הופכת כפל (של הבסיסים) לסכום (של המעריכים). בדומה, היא יכולה גם להפוך סכום (של המעריכים) לכפל (של הבסיסים). אז עכשיו בואו ניקח את נוסחת אוילר ונציב במעריך שלה את הסכום {% equation %}\alpha+\beta{% endequation %}:

{% equation %}e^{i\left(\alpha+\beta\right)}=\cos\left(\alpha+\beta\right)+i\sin\left(\alpha+\beta\right){% endequation %}

אם נצליח למצוא ייצוג יותר נחמד ל-{% equation %}e^{i\left(\alpha+\beta\right)}{% endequation %}, זה יניב לנו <strong>שתי</strong> נוסחאות בבת אחת - גם עבור סינוס של סכום זוויות וגם עבור קוסינוס של סכום זוויות. כדי לראות את זה קורה, בואו נשתמש ב"סכום של מעריכים מתורגם למכפלת הבסיסים":

{% equation %}e^{i\left(\alpha+\beta\right)}=e^{i\alpha}\cdot e^{i\beta}=\left(\cos\alpha+i\sin\alpha\right)\left(\cos\beta+i\sin\beta\right){% endequation %}

עכשיו, איך נפתח את מכפלת הסוגריים שמופיעה באגף ימין? כמו שתמיד פותחים מכפלת סוגריים - נקבל ארבעה איברים:

{% equation %}\cos\alpha\cos\beta+i\sin\alpha\cos\beta+i\cos\alpha\sin\beta+i^{2}\sin\alpha\sin\beta{% endequation %}

נשתמש בכך ש-{% equation %}i^{2}=-1{% endequation %}, נקבץ איברים ונקבל:

{% equation %}\left(\cos\alpha\cos\beta-\sin\alpha\sin\beta\right)+i\left(\sin\alpha\cos\beta+\cos\alpha\sin\beta\right){% endequation %}

עכשיו נשווה את מה שקיבלנו אל הביטוי המקורי:

{% equation %}\cos\left(\alpha+\beta\right)+i\sin\left(\alpha+\beta\right){% endequation %}

אם נסתכל על האיברים שמוכפלים ב-{% equation %}i{% endequation %} בשני הביטויים ונשווה אותם, נקבל

{% equation %}\sin\left(\alpha+\beta\right)=\sin\alpha\cos\beta+\cos\alpha\sin\beta{% endequation %}

ואם נסתכל על האיברים שלא מוכפלים ב-{% equation %}i{% endequation %} ונשווה אותם, נקבל

{% equation %}\cos\left(\alpha+\beta\right)=\cos\alpha\cos\beta-\sin\alpha\sin\beta{% endequation %}

וזהו, זה מסיים את פיתוח הנוסחאות הללו - בלי לצייר משולשים ובלי שום דבר אחר. והחלק היפה ביותר כאן הוא שזו הוכחה <strong>פורמלית לחלוטין</strong> אם כבר הוכחנו את נוסחת אוילר. אבל כפי שאמרתי - בשביל הפיתוח הקצרצר שעשיתי כרגע לא צריך לדעת למה נוסחת אוילר נכונה או אפילו להכיר לעומק את הרכיבים שלה. אפשר לחשוב עליה בתור טריק כדי לזכור בקלות את הנוסחאות הטריגונומטריות ותו לא. עם זאת, לטעמי עיקר הכיף פה הוא בדיוק בקלות שבה הכל נובע, וכמה "ברור" מאיפה כל רכיב בנוסחאות הטריגונומטריות מגיע פתאום.

<h2>אז למה נוסחת אוילר נכונה?</h2>

החלק הזה יהיה מין "חלק בונוס". אני אזרוק הסברים מטורללים מהשרוול בלי להיכנס לעובי ההוכחות, ובהחלט ייתכן שתאבדו אותי פה; אבל אם נצא מכאן עם מושג כללי לגבי מה הולך פה ועד כמה מתחבאים מתחת לפני השטח של המתמטיקה דברים מגניבים, התקדמנו.

לב העניין הוא בהצגה של פונקציות מסויימות בתור <strong>טורי טיילור</strong>. טור טיילור הוא סכום אינסופי של מחוברים, ש... למה אני מדבר כל כך הרבה, הנה הטורים:

<ul> <li>{% equation %}e^{x}=1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\frac{x^{4}}{4!}+\ldots=\sum_{n=0}^{\infty}\frac{x^{n}}{n!}{% endequation %}</li>


<li>{% equation %}\sin x=x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\frac{x^{7}}{7!}+\ldots=\sum_{n=0}^{\infty}\left(-1\right)^{n}\frac{x^{2n+1}}{\left(2n+1\right)!}{% endequation %}</li>


<li>{% equation %}\cos x=1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\frac{x^{6}}{6!}+\ldots=\sum_{n=0}^{\infty}\left(-1\right)^{n}\frac{x^{2n}}{\left(2n\right)!}{% endequation %}</li>

</ul>

המשמעות של הטורים הללו היא שככל שנחבר יותר מחוברים, כך נתקרב יותר ויותר לערך ה"אמיתי" של הביטוי באגף שמאל. בגלל שהמכנה של המחוברים הולך וגדל במהירות (כי ככה זו פונקציית עצרת), עבור ערכים לא גדולים של {% equation %}x{% endequation %} לא נזדקק לחיבור של <strong>יותר מדי</strong> מחוברים. למשל, עבור {% equation %}x=3{% endequation %} אני יכול לחשב ידנית מה זה {% equation %}e^{3}{% endequation %}: מכיוון ש-{% equation %}e\approx2.71828{% endequation %} אני אקח מחשבון, אכפול את {% equation %}2.71828{% endequation %} פעמיים בעצמו ואקבל {% equation %}20.085496391455552{% endequation %}. עכשיו אני אלך אל הטור {% equation %}1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\frac{x^{4}}{4!}+\ldots{% endequation %}, אציב {% equation %}x=3{% endequation %} ואתחיל לחבר איברים:

{% equation %}1+3+\frac{9}{2}+\frac{27}{6}+\frac{81}{24}+\frac{243}{120}+\frac{729}{720}+\frac{2187}{5040}{% endequation %}

למה אני עוצר ב-{% equation %}\frac{3^{7}}{7!}=\frac{2187}{5040}{% endequation %}? כי האיבר הבא כבר יהיה די קטן, כי את המונה אני כופל ב-3 אבל את המכנה אני אכפול ב-8 - אני אקבל איבר שהוא פחות מ-{% equation %}0.2{% endequation %} ונראה לי שהבנו את הקטע.

אחרי שאני מחבר את כל המספרים הללו אני אקבל {% equation %}20.063392857142855{% endequation %} שכבר מאוד קרוב אל המספר שאני מצפה לקבל - ועוד כמה איברים בטור יניבו לי מספרים כמעט זהים. אז הנוסחה באמת עובדת יפה עבור הפונקציה {% equation %}e^{x}{% endequation %}.

מה עם {% equation %}\sin x{% endequation %}? ובכן, מדגדג להציב {% equation %}x=90^{\circ}{% endequation %} ולראות איך מקבלים את 1 אבל שום דבר כזה לא יקרה. למעשה, נקבל מספר גדול בצורה מפחידה. מה עשינו לא נכון? ובכן, הנוסחה לעיל <strong>לא</strong> נכונה עבור סינוס אם אנחנו מודדים את הזוויות במעלות. בשביל שהיא תעבוד, אנחנו <strong>חייבים</strong> למדוד את הזוויות באמצעות משהו שנקרא <strong>רדיאנים</strong>. לא כזה חשוב מה ההגדרה המדויקת של רדיאן (כמות הרדיאנים בזווית מסויימת שווה לאורך הקשת של מעגל היחידה שנשענת על הזווית הזו; <a href="https://gadial.net/2008/01/11/radians/">יש לי פוסט בנושא</a>) אלא איך "מתרגמים" מעלות לרדיאנים. הכלל פשוט מאוד: מחלקים ב-{% equation %}360{% endequation %} וכופלים ב-{% equation %}2\pi{% endequation %}, כי 360 מעלות זה היקף מעגל שלם במעלות, ואילו {% equation %}2\pi{% endequation %} זה היקף מעגל שלם ברדיאנים (אפשר כמובן גם לחלק ב-180 ולכפול ב-{% equation %}\pi{% endequation %}; אותו אפקט). אז במקרה שלנו, זווית של תשעים מעלות שווה ל-{% equation %}\frac{\pi}{2}\approx1.5708{% endequation %} רדיאנים. בואו ננסה להציב <strong>את זה</strong> בנוסחה:

{% equation %}\frac{\pi}{2}-\frac{1}{6}\left(\frac{\pi}{2}\right)^{3}+\frac{1}{120}\left(\frac{\pi}{2}\right)^{5}\approx1.0045{% endequation %}

זה... קירוב לא רע בכלל של 1! וזה יילך וישתפר ככל שנחבר עוד איברים. אני אחסוך מאיתנו את הניסוי עבור קוסינוס - זה יעבוד גם שם. כלומר, עוד לפני שמגיעים לנוסחת אוילר כבר יש לנו משהו נחמד מאוד - שיטה פרקטית לחשב את סינוס וקוסינוס בצורה טובה מאוד. כשאני למדתי טריגונומטריה בבית הספר ראיתי המון זהויות טריגונומטריות, אבל שום הסבר על איך אפשר לחשב את הפונקציות הטריגונומטריות בפועל.

כמובן, זו שאלה מצויינת מאיפה הנוסחאות הללו בכלל הגיעו ולמה הן נכונות. התשובה היא שאם מאמצים את ההגדרה שלנו לסינוס וקוסינוס, צריך להשתמש בכלים מ<strong>חשבון דיפרנציאלי</strong> כדי להגיע אל הנוסחאות הללו; ספציפית, צריך <strong>לגזור</strong> שוב ושוב את הפונקציות ולהשתמש בנוסחה הכללית למציאת טור טיילור של משהו ({% equation %}f\left(x-x_{0}\right)\approx\sum_{n=0}^{\infty}f^{\left(n\right)}\left(x_{0}\right)\frac{\left(x-x_{0}\right)^{n}}{n!}{% endequation %} כאשר {% equation %}f^{\left(n\right)}{% endequation %} מייצג את הנגזרת ה-{% equation %}n{% endequation %}-ית ו-{% equation %}x_{0}{% endequation %} היא נקודה שסביבה בוחרים לפתח את טור הטיילור; במקרה של הטורים למעלה בחרנו {% equation %}x_{0}=0{% endequation %}). תשובה אחרת, שבמבט ראשון נשמעת מוזרה למדי, היא שרוב מי שרוצים להגדיר פורמלית סינוסים וקוסינוסים מגדירים אותם <strong>מלכתחילה</strong> בתור הטורים הללו ולא בעזרת הגדרות גאומטריות. יש לכך יתרונות; ההגדרה הזו הרבה יותר פורמלית. אבל כמובן, אי אפשר ללמד הגדרה כזו בבית הספר. אני עצמי בחרתי להציג בבלוג הגדרה לסינוסים וקוסינוסים שהיא סוג של אמצע הדרך בין שתי הגישות - להגדיר אותם בתור פתרונות של <strong>משוואה דיפרנציאלית</strong> (<a href="https://gadial.net/2010/03/31/sine_and_cosine_via_ode/">הנה הפוסט</a>). בצורה הזו נהנים משני העולמות - גם מתבססים על חשבון דיפרנציאלי שלא נגיש בכלל בתיכון וגם נותנים תחושה שמשהו פה לא פורמלי עד הסוף.

נחזור אל טורי הטיילור שלנו. אם נסתכל עליהם קצת נראה שהם מאוד דומים. הטור של {% equation %}e^{x}{% endequation %} מכיל איברים שאחר כך מתפזרים לשתי קבוצות ("החזקות הזוגיות" ו"החזקות האי זוגיות") ומופיעים אצל קוסינוס (הזוגיות) וסינוס (האי זוגיות), רק ששם יש להן סימן מינוס לפעמים. כלומר, כבר עכשיו אפשר לחשוב שיש פה קשר חזק - נוסחת אוילר זה לא סתם איזו הגדרה אקראית נטולת פשר.

הרעיון הוא לקחת את הנוסחה עבור {% equation %}e^{x}{% endequation %}, שבמקור מוכיחים את הנכונות שלה רק עבור ערכי {% equation %}x{% endequation %} ממשיים, ולהציב בה את הערך {% equation %}x=i\alpha{% endequation %}, שהוא <strong>מספר מרוכב</strong>. כרגיל, אני חוסך מכם את ההוכחה הפורמלית שאפשר לעשות את זה (וכרגיל, אני מזהיר אתכם שמתמטיקאים אוהבים <strong>להגדיר</strong> את הפונקציה {% equation %}e^{x}{% endequation %} ככה מראש גם עבור מרוכבים, מה שהופך את נוסחת אוילר פשוט ל<strong>הגדרה</strong> וזה לא משהו שעושה לנו נעים לאינטואיציה גם אם זה נטוע עמוק בתובנות מתמטיות אמיתיות) - בואו פשוט נראה מה קורה.

כזכור, אמרתי ש-{% equation %}i{% endequation %} הוא מספר בעל התכונה ש-{% equation %}i^{2}=-1{% endequation %}. אז מה זה {% equation %}i^{3}{% endequation %}? פשוט מאוד: {% equation %}i^{3}=i^{2}\cdot i=-i{% endequation %}. ומה זה {% equation %}i^{4}{% endequation %}? שוב, פשוט מאוד: {% equation %}i^{4}=\left(i^{2}\right)^{2}=\left(-1\right)^{2}=1{% endequation %}. כלומר, אם מסתכלים על חזקות של {% equation %}i{% endequation %} רואים איזו שהיא מחזוריות כאן:

{% equation %}i^{0},i^{1},i^{2},i^{3},i^{4},i^{5},i^{6},i^{7},i^{8},\ldots{% endequation %}

הופך ל

{% equation %}1,i,-1,-i,1,i,-1,-i,1,\ldots{% endequation %}

זה בדיוק מה שיקרה כשנציב את {% equation %}i\alpha{% endequation %} בטור של האקספוננט. חצי מהמחוברים יהיו מהצורה "{% equation %}i{% endequation %} כפול משהו" והחצי השני מהצורה "1 כפול משהו", כשהמשהו מזפזפ בין להיות בלי מינוס ולהיות עם מינוס:

{% equation %}e^{i\alpha}=1+\left(i\alpha\right)+\frac{\left(i\alpha\right)^{2}}{2!}+\frac{\left(i\alpha\right)^{3}}{3!}+\frac{\left(i\alpha\right)^{4}}{4!}+\ldots{% endequation %}

{% equation %}=1+i\alpha-\frac{\alpha^{2}}{2!}-i\frac{\alpha^{3}}{3!}+\frac{\alpha^{4}}{4!}+\ldots{% endequation %}

את הטור הזה אפשר "לפצל לשניים" (שוב, זה דורש הוכחה):

{% equation %}1+i\alpha-\frac{\alpha^{2}}{2!}-i\frac{\alpha^{3}}{3!}+\frac{\alpha^{4}}{4!}+\ldots=\left(1-\frac{\alpha^{2}}{2!}+\frac{\alpha^{4}}{4!}+\ldots\right)+i\left(\alpha-\frac{\alpha^{3}}{3!}+\ldots\right){% endequation %}

וקיבלנו את שני הטורים עבור סינוס וקוסינוס:

{% equation %}\left(1-\frac{\alpha^{2}}{2!}+\frac{\alpha^{4}}{4!}+\ldots\right)+i\left(\alpha-\frac{\alpha^{3}}{3!}+\ldots\right)=\cos\alpha+i\sin\alpha{% endequation %}

זה "מוכיח" את נוסחת אוילר ומסיים את הסיפור כאן מבחינתנו.

ועכשיו וידוי קטן לסיום: גדי של התיכון תיעב טריגונומטריה (את זה כבר סיפרתי) ובאופן כללי לא אהב מתמטיקה במיוחד, אבל אי שם באמצע כיתה י"ב, אחרי אחד השיעורים, המורה שלו לפיזיקה הראה לנו את העניין הזה של טורי טיילור ונוסחת אוילר שהראיתי כאן. נראה לי שזו הייתה הפעם הראשונה שראיתי מתמטיקה שחורגת מחומר הלימוד של בית הספר ועם זאת עדיין קרובה אליו מספיק כדי שאוכל "להרגיש" אותה בידיים (כלומר לשבת, לעשות את החישובים בעצמי, לראות שזה יוצא ולהתמוגג). תחושת הפליאה הזו הייתה גם מה שהכווין אותי ללמוד מתמטיקה בהמשך (במקביל ללימודי מדעי המחשב שאליהם הגעתי בזכות הספר "אלגוריתמיקה" של דוד הראל). אני מקווה שהצלחתי להעביר חלק מתחושת הפליאה הזו לאלו ששרדו עד כאן. 
