---
title: "אז איך פותרים אינטגרלים בתיכון?"
layout: post
categories:
  - אנליזה מתמטית
tags:
  - אינטגרלים
social_media_share: true
---


<h2>מבוא</h2>

ביקשו ממני לכתוב פוסט על איך פותרים תרגילים עם אינטגרלים ברמת תיכון, ואני מאוד שמח לעשות את זה כי זה נושא שחביב עלי מאוד מסיבה פשוטה: לחשב אינטגרלים זה <strong>קשה</strong>. בגלל שזה קשה, פשוט <strong>אי אפשר</strong> לתת בתיכון תרגילים קשים <strong>באמת</strong> שמערבים אינטגרלים, ולכן מה שכן נותנים הוא את הדברים הפשוטים יחסית שאפשר לפתור בצורה די מסודרת אחרי שמבינים מה בעצם הולך שם, מה זה אינטגרלים ואיך ניגשים לטכניקה שלהם.

נתחיל מ"מה זה אינטגרלים". חלק מהסיבה שבגללה אינטגרלים זה עסק מבלבל הוא שאנחנו משתמשים ב"אינטגרל" כדי לתאר שני דברים שנראים במבט ראשון שונים לגמרי, אבל אחת מהתוצאות היפות במתמטיקה ("המשפט היסודי של החשבון הדיפרנציאלי והאינטגרלי") מראה שהם קשורים בצורה חזקה. ראשית, אינטגרלים מוצגים בתור "ההפך <strong>מנגזרת</strong>", כלומר בתור מושג שכדי להבין אותו צריך קודם כל להבין את המושג המרכזי השני בחשבון דיפרנציאלי ואינטגרלי - הנגזרת. יש לי <a href="https://gadial.net/2010/11/21/derivative/">פוסטים</a> על נגזרות ו<a href="https://gadial.net/2010/12/01/deriving_ourselves_to_death/">על איך מחשבים אותן</a>, כך שבפוסט הזה אניח היכרות בסיסית עם הנושא; אבל אני <strong>כן</strong> הולך להזכיר כל דבר רלוונטי לפני שאני משתמש בו.

לאינטגרל שהוא "ההפך מנגזרת" קוראים "אינטגרל לא מסויים". יש גם מושג אחר, של "אינטגרל מסויים", שבכלל עוסק בחישוב של שטחים, נפחים וכל מני דברים מספריים אחרים. זו, מבחינה היסטורית, הנקודה שבה מושג האינטגרל נולד, ו<a href="https://gadial.net/2010/11/27/integral/">יש לי פוסט</a> שמסביר את מושג האינטגרל מנקודת המבט הזו. אלא שהפוסט הנוכחי הולך להיות טכני ברמת תיכון, מה שאומר שלא נצטרך לדבר הרבה על אינטגרל מסויים. ההגדרה הפורמלית שלו? דורשת טכניקה שלא נלמדת בתיכון. האינטואיציה הכללית מאחוריו? דורשת רעיונות שלא נלמדים בתיכון. מה שנשאר זה רק איך מחשבים אותו בהקשרים ספציפיים, וזה קל ונגיע לזה. החישוב הוא תמיד "תחשבו את האינטגרל <strong>הלא מסויים</strong> ואז תעשו איתו דברים", כך שהמושג הטכני שרלוונטי לנו הוא אינטגרל לא מסויים.

<h2>פרק ראשון, שבו נספר על נגזרות ואינטגרלים של פולינומים</h2>

אם נלך לדף הנוסחאות בבגרות ונלך אל "אינטגרלים", נראה קודם כל את הנוסחה המייאשת הבאה:

<ul> <li>{% equation %}\int x^{t}dx=\frac{x^{t+1}}{t+1}+C{% endequation %} ({% equation %}t{% endequation %} ממשי, {% equation %}t\ne-1{% endequation %})</li>

</ul>

אחרי שנבין אותה, נעבור כבר יותר מחצי מהדרך אל הבנת אינטגרלים באופן כללי. אבל כדי להבין אותה, צריך לדבר קודם כל על <strong>נגזרת</strong>. נגזרת זה משהו שעושים לפונקציות, כשאצלנו פונקציה היא משהו שמקבל <strong>קלט</strong> {% equation %}x{% endequation %} ומוציא <strong>פלט</strong> שכותבים בתור איזו שהיא נוסחה שמערבת את {% equation %}x{% endequation %}. למשל {% equation %}2x^{3}+5{% endequation %} זו דרך מקוצרת לכתוב את הפונקציה {% equation %}y=2x^{3}+5{% endequation %} (או {% equation %}f\left(x\right)=2x^{3}+5{% endequation %}; מה שיטות הסימון של הצעירים בימינו?). הנגזרת של פונקציה אמורה לייצג את "קצב ההשתנות" שלה עבור ערכים שונים ומשונים של {% equation %}x{% endequation %}; זה שייך לתיאוריה שלא רלוונטית לפוסט הטכני הזה. הנקודה הרלוונטית היא ש<strong>הנגזרת של פונקציה היא בעצמה פונקציה</strong> ושגזירה של פונקציה היא משהו שיש לנו דרך שיטתית מאוד לבצע.

הדברים שהכי קל לגזור הם פונקציות שנקראות <strong>פולינומים</strong>. פולינומים הם יצורים כמו {% equation %}2x^{3}+5{% endequation %}: סכום של איברים שכל איבר הוא מהצורה "מספר כלשהו כפול חזקה שלמה של {% equation %}x{% endequation %}" (בדוגמא שלי {% equation %}5{% endequation %} מוכפל בחזקה {% equation %}x^{0}{% endequation %} של {% equation %}x{% endequation %}). הנה הנגזרות של כמה פולינומים ממש פשוטים:

<ul> <li>הנגזרת של הפולינום {% equation %}1{% endequation %} היא 0.</li>


<li>הנגזרת של הפולינום {% equation %}x{% endequation %} היא 1.</li>


<li>הנגזרת של הפולינום {% equation %}x^{2}{% endequation %} היא {% equation %}2x{% endequation %}.</li>


<li>הנגזרת של הפולינום {% equation %}x^{3}{% endequation %} היא {% equation %}3x^{2}{% endequation %}.</li>


<li>הנגזרת של הפולינום {% equation %}x^{4}{% endequation %} היא {% equation %}4x^{3}{% endequation %}.</li>

</ul>

ונראה לי שכבר הבנו את הרעיון, לא? באופן כללי את כל אלו אפשר לתאר על ידי "הנגזרת של {% equation %}x^{t}{% endequation %} היא {% equation %}tx^{t-1}{% endequation %}", וזה יהיה נכון לכל מספר ממשי {% equation %}t{% endequation %}, גם אם הוא לא מספר שלם בכלל (למשל, הנגזרת של {% equation %}x^{\pi}{% endequation %} היא {% equation %}\pi x^{\pi-1}{% endequation %}). זה זמן טוב להציג את הסימון של נגזרת - משתמשים במשהו שנקרא "תג" ובקושי אפשר לראות אותו, כי למה לא לבלבל אנשים אם אפשר. הנה איך נראית הנוסחה הכללית שראינו כשמסמנים אותה עם תג:

<ul> <li>{% equation %}\left(x^{t}\right)^{\prime}=tx^{t-1}{% endequation %}</li>

</ul>

גם זו נוסחה שמופיעה בדף הנוסחאות, וזו נקודת המוצא שלנו. בואו נבין איך היא מתקשרת לנוסחה המוזרה עבור אינטגרלים שראינו קודם ואנחנו עדיין לא מבינים.

כזכור, אינטגרל <strong>לא מסויים</strong> הוא "ההפך מנגזרת". אם הנגזרת של {% equation %}x^{2}{% endequation %} היא {% equation %}2x{% endequation %}, זה אומר שהאינטגרל הלא מסויים של {% equation %}2x{% endequation %} יהיה {% equation %}x^{2}{% endequation %}. באופן דומה, האינטגרל הלא מסויים של {% equation %}3x^{2}{% endequation %} יהיה {% equation %}x^{3}{% endequation %} וכן הלאה. פרט לכך, כשכותבים אינטגרל לא מסויים תמיד מוסיפים לו {% equation %}+C{% endequation %} בסוף. כלומר, אני כותב {% equation %}\int2xdx=x^{2}+C{% endequation %} ו-{% equation %}\int3x^{2}dx=x^{3}+C{% endequation %}. הסיבה לכך היא שאותה נגזרת יכולה להתקבל <strong>מכמה פונקציות שונות</strong>, שההבדל ביניהן הוא חיבור של מספר קבוע. למשל, גם הנגזרת של {% equation %}x^{3}+5{% endequation %} היא {% equation %}3x^{2}{% endequation %}; בהמשך גם נבין למה. מבחינה טכנית, המשמעות היא זו: בשביל למצוא אינטגרל לא מסויים של פונקציה {% equation %}f{% endequation %} מספיק למצוא פונקציה {% equation %}F{% endequation %} <strong>אחת</strong> כך ש-{% equation %}F^{\prime}=f{% endequation %}, ואז האינטגרל הלא מסויים הכללי הוא פשוט {% equation %}F+C{% endequation %}, כלומר כותבים {% equation %}\int fdx=F+C{% endequation %}.

עכשיו, לחישוב נגזרת יש שתי תכונות נחמדות <strong>מאוד</strong> שנקראות ביחד "הלינאריות של הנגזרת". התכונה הראשונה היא ש-{% equation %}\left(f+g\right)^{\prime}=f^{\prime}+g^{\prime}{% endequation %}, כלומר כדי לחשב את הנגזרת של סכום שתי פונקציות מספיק לחשב את הנגזרת של כל אחת בנפרד, ורק אז לחבר; והתכונה השניה היא ש-{% equation %}\left(c\cdot f\right)^{\prime}=c\cdot f^{\prime}{% endequation %} עבור מספר ממשי {% equation %}c{% endequation %}. כלומר, כדי לחשב את הנגזרת של "קבוע כפול פונקציה" מספיק לחשב את הנגזרת של הפונקציה, ואז לכפול בקבוע הזה.

עכשיו אפשר לחשב בקלות את הנגזרת של כל פולינום: למשל, מה הנגזרת של {% equation %}5{% endequation %}? מכיוון ש-{% equation %}5=5\cdot1{% endequation %} ואנחנו יודעים ש-{% equation %}\left(1\right)^{\prime}=0{% endequation %} נקבל ש-{% equation %}\left(5\right)^{\prime}=5\cdot\left(1\right)^{\prime}=5\cdot0=0{% endequation %} ("הנגזרת של כל קבוע היא אפס"). ומה הנגזרת של {% equation %}2x^{3}{% endequation %}? מכיוון שהנגזרת של {% equation %}x^{3}{% endequation %} היא {% equation %}3x^{2}{% endequation %}, נקבל ש-{% equation %}\left(2x^{3}\right)^{\prime}=2\left(3x^{2}\right)=6x^{2}{% endequation %}. ועכשיו, מה הנגזרת של {% equation %}2x^{3}+5{% endequation %}? נשתמש בתכונה עם החיבור ונקבל ש-{% equation %}\left(2x^{3}+5\right)^{\prime}=\left(2x^{3}\right)^{\prime}+\left(5\right)^{\prime}=6x^{2}+0=6x^{2}{% endequation %}. הנה לנו ההסבר לעניין ה-{% equation %}+C{% endequation %}; באופן כללי, {% equation %}\left(f+C\right)^{\prime}=f^{\prime}+0=f^{\prime}{% endequation %} ולכן כל הפונקציות מהצורה {% equation %}f+C{% endequation %} עבור כל {% equation %}C{% endequation %} ממשי יתנו את אותה הנגזרת.

איך זה עוזר לנו לחשב אינטגרלים?

ובכן, אם {% equation %}\left(x^{2}\right)^{\prime}=2x{% endequation %}, אז אפשר עכשיו <strong>לחלק ב-</strong><strong>2</strong> את שני האגפים ולקבל {% equation %}\left(\frac{1}{2}x^{2}\right)^{\prime}=x{% endequation %}. באופן דומה אפשר לטפל ב-{% equation %}x^{3}{% endequation %}: אם {% equation %}\left(x^{3}\right)^{\prime}=3x^{2}{% endequation %} אז {% equation %}\left(\frac{1}{3}x^{3}\right)^{\prime}=x^{2}{% endequation %}, וכך גם לנגזרות אחרות. בואו נכתוב את זה בעזרת סימונים של אינטגרלים:

{% equation %}\int xdx=\frac{1}{2}x^{2}+C{% endequation %}

{% equation %}\int x^{2}dx=\frac{1}{3}x^{3}+C{% endequation %}

ומה קורה באופן כללי? ובכן, {% equation %}\left(x^{t}\right)^{\prime}=tx^{t-1}{% endequation %}, ולכן נקבל:

{% equation %}\int x^{t-1}dx=\frac{1}{t}x^{t}+C{% endequation %}

אלא שכאן <strong>צריך להיזהר</strong>. כאשר {% equation %}t=0{% endequation %}, יש לנו בביטוי הזה חלוקה באפס - זה פשוט לא עובד! המקרה הזה מגיע מהנוסחה הבאה: {% equation %}\left(x^{0}\right)^{\prime}=0\cdot x^{-1}{% endequation %}. במקרה הזה, אי אפשר לחלק בקבוע {% equation %}0{% endequation %} שבו מוכפל {% equation %}x^{-1}{% endequation %} ולכן לא ניתן "לחלץ" אותו - זה מקרה פרטי מיוחד שנדבר עליו בהמשך.

עכשיו, בואו ניקח את הנוסחה {% equation %}\int x^{t-1}dx=\frac{1}{t}x^{t}+C{% endequation %} ונשנה אותה טיפה. בדרך כלל כשאני רוצה למצוא אינטגרל עבור משהו, זה לא עבור {% equation %}x^{t-1}{% endequation %} אלא עבור {% equation %}x^{t}{% endequation %} (כלומר, אני לא כותב את החזקה בתור "משהו פחות 1"). אז בואו נעשה "החלפת משתנה": נסמן {% equation %}s=t-1{% endequation %}, כלומר {% equation %}t=s+1{% endequation %}, ואז נקבל את הנוסחה {% equation %}\int x^{s}dx=\frac{1}{s+1}x^{s+1}+C{% endequation %}. מכיוון ש-{% equation %}s{% endequation %} זה סתם סימון, אפשר "לחזור" אל {% equation %}t{% endequation %}, ובאותה הזדמנות קצת לכווץ את אגף ימין, ולקבל

<ul> <li>{% equation %}\int x^{t}dx=\frac{x^{t+1}}{t+1}+C{% endequation %}</li>

</ul>

זו הנוסחה שהזכרנו קודם. שימו לב מה עכשיו המקרה ה"אסור": קודם זה היה {% equation %}t=0{% endequation %}, אבל אחרי החלפת המשתנים זה עבר להיות המקרה {% equation %}t=-1{% endequation %} (קל לראות את זה - זה מה שיגרום למכנה באגף ימין להתאפס). לכן מסייגים את הנוסחה ההיא בכך ש-{% equation %}t\ne-1{% endequation %}.

עכשיו אפשר להשתמש בנוסחה הזו כדי לחשב אינטגרלים קצת יותר מורכבים, כשאנחנו נעזרים בתכונה משמחת אחת: בזכות העובדה שנגזרת היא <strong>לינארית</strong>, גם אינטגרל הוא כזה. כלומר: {% equation %}\int\left(f+g\right)dx=\int fdx+\int gdx{% endequation %} ו-{% equation %}\int cfdx=c\int fdx{% endequation %}. לכן, אם למשל אני רוצה לחשב את האינטגרל של {% equation %}2x^{3}+5{% endequation %}, אני משתמש בלינאריות ומקבל: 

{% equation %}\int\left(2x^{3}+5\right)dx=2\int x^{3}dx+5\int1\cdot dx=\frac{2x^{4}}{4}+5x+C=\frac{x^{4}}{2}+5x+C{% endequation %}

אפשר לעצור לסיכום ביניים קצר: אנחנו מבינים (אני מקווה!) את הנוסחה המוזרה מדף הנוסחאות, ואיך אפשר להשתמש בה כדי לחשב אינטגרל עבור <strong>כל</strong> פולינום, חוץ מהמקרה המעצבן הזה של {% equation %}x^{-1}{% endequation %} שאין לנו מושג מה לעשות בו. אפשר עכשיו לעבור לדברים מתוחכמים קצת יותר.

<h2>פרק שני, שבו אנחנו עוברים לדברים מתוחכמים קצת יותר</h2>

יודעות מה? בעצם לא. אולי לא כדאי לשפוך את כל מהומת האינטגרלים הלא מסויימים על הראש בבת אחת. במקום זה, בואו נראה איך משתמשים במה שכבר יש לנו כדי לטפל באינטגרלים <strong>מסויימים</strong>, ברמה שמספיקה לפתור שאלות מהבגרות. אם כן:

<h2>פרק שני האמיתי באמת שבו אנחנו עוברים לחשב שטחים</h2>

היי, תראו, הנה שאלה אמיתית מבגרות!

<img src="{{site.baseurl}}{{site.post_images}}/2020/07/IntegralQuestion1.PNG" alt=""/>

בשאלה הזו מעורבות שתי פונקציות שהן <strong>פולינומים</strong>, כלומר שאנחנו כבר יודעים לטפל בהן. פונקציה אחת היא {% equation %}f\left(x\right)=x^{2}-6x+5{% endequation %}, והשניה היא {% equation %}g\left(x\right)=x^{2}-10x+a{% endequation %} כאשר {% equation %}a{% endequation %} הוא "פרמטר" שבעצם תחילת השאלה עוסקת במציאת הערך המדויק שלו. אין פה משהו מעניין - אומרים ששתי הפונקציות הללו נחתכות בדיוק בנקודה שקואורדינטת ה-{% equation %}x{% endequation %} שלה היא {% equation %}4{% endequation %}. זה אומר שאם נציב {% equation %}4{% endequation %} בשני הפולינומים, הערך שאנחנו מקבלים אמור להיות שווה, כלומר {% equation %}f\left(x\right)=g\left(x\right){% endequation %}. בואו נפשט את השוויון ובסוף נציב {% equation %}x=4{% endequation %}:

{% equation %}x^{2}-6x+5=x^{2}-10x+a{% endequation %} (זה {% equation %}f\left(x\right)=g\left(x\right){% endequation %})

{% equation %}4x+5=a{% endequation %} (העברתי את {% equation %}x^{2}-10x{% endequation %} לאגף שמאל)

{% equation %}4\cdot4+5=a{% endequation %} (הצבתי {% equation %}x=4{% endequation %})

{% equation %}a=21{% endequation %} (זו המסקנה)

כלומר, {% equation %}g\left(x\right)=x^{2}-10x+21{% endequation %}. אגב, נקודת החיתוך של שני הפולינומים היא {% equation %}\left(4,-3\right){% endequation %}.

עכשיו צריך למצוא את השטח ש"מוגבל על ידי הגרפים של שתי הפונקציות", אבל בשביל לעשות את זה קודם כל צריך להבין איך בכלל משתמשים באינטגרל כדי למצוא שטחים, ולשם כך בואו נתחיל מהמקרה הכי פשוט שמתואר באיור הבא:

<img src="{{site.baseurl}}{{site.post_images}}/2020/07/Integral1.PNG" alt=""/>

כאן יש לנו פונקציה {% equation %}f\left(x\right){% endequation %} שאני מסתכל עליה אך ורק בין שתי נקודות {% equation %}a,b{% endequation %}. כלומר, אני מצייר את {% equation %}f\left(x\right){% endequation %} רק עבור {% equation %}a\le x\le b{% endequation %}. אני מותח שני קווים אנכיים, אחד בנקודה {% equation %}a{% endequation %} (עד לגובה {% equation %}f\left(a\right){% endequation %}) והשני בנקודה {% equation %}b{% endequation %} (עד לגובה {% equation %}f\left(b\right){% endequation %}), ואז אני צובע בתכלת את האיזור ש"כלוא" בין ארבעה קווים: שני הקווים האנכיים הללו שציירתי, ציר ה-{% equation %}x{% endequation %} (הקו האופקי מ-{% equation %}\left(a,0\right){% endequation %} עד {% equation %}\left(b,0\right){% endequation %}) ולסיום, ה"קו" (ליתר דיוק, ה<strong>עקום</strong>) למעלה שמתאים ל-{% equation %}f{% endequation %}. שימו לב לכך ש-{% equation %}f\left(x\right){% endequation %} היא <strong>אי-שלילית</strong> בכל הקטע הזה.

בהינתן כל אלו, השטח שצבעתי בתכלת שווה למה שנקרא <strong>האינטגרל המסויים</strong> של {% equation %}f{% endequation %} בין {% equation %}a{% endequation %} ל-{% equation %}b{% endequation %}. הדבר הזה מסומן ב-{% equation %}\int_{a}^{b}f\left(x\right)dx{% endequation %}. קישרתי קודם לפוסט שלי שבו אני מסביר מה זה אינטגרל מסויים <strong>באמת</strong> (אפשר לחשוב עליו בתור סוג מתוחכם של סכום <strong>מאוד אינסופי</strong>), אבל אנחנו לא צריכים את ההגדרה הזו כדי לחשב שטחים, רק להבין איך אפשר להיעזר באינטגרל המסויים כדי לחשב אותם.

אז... איך אני מחשב את המספר {% equation %}\int_{a}^{b}f\left(x\right)dx{% endequation %}? פשוט מאוד, בעזרת האינטגרל <strong>הלא מסויים</strong>. נניח ש-{% equation %}\int f\left(x\right)dx=F\left(x\right)+C{% endequation %}, כלומר {% equation %}F{% endequation %} היא פונקציה שכאשר גוזרים אותה מקבלים את {% equation %}f{% endequation %}. אז מתקיים הקשר הבא, שבעיני הוא מדהים ומרהיב ואחד מהדברים הנפלאים במתמטיקה: {% equation %}\int_{a}^{b}f\left(x\right)dx=F\left(b\right)-F\left(a\right){% endequation %}. כלומר, כדי לחשב את האינטגרל המסויים של {% equation %}f{% endequation %} (ובדוגמא שלנו, את השטח ה"מופרע" בצבע תכלת), צריך לחשב את הערך של {% equation %}F{% endequation %} <strong>בשתי נקודות בלבד</strong>, אלו של קצוות הקטע שעליו עושים אינטגרל ואז לחסר את הערך הראשון מהשני. הדבר הנפלא הזה הוא תוצאה של מה שמכונה "המשפט היסודי של החדו"א" והאינטואיציה פה היא שהאינטגרל המסוים (השטח בתכלת) מייצג בדיוק את "כמה שינוי {% equation %}F{% endequation %} צריכה להשתנות החל מהנקודה {% equation %}a{% endequation %} כדי להגיע לערכה בנקודה {% equation %}b{% endequation %}", אבל לא קריטי להבין את האינטואיציה הזו לצרכים הטכניים.

הכל טוב ויפה, אבל עכשיו - איך משתמשים בזה כדי לפתור את השאלה שהצגתי לעיל? שם מבקשים שטח שכלוא בין <strong>שתי</strong> עקומות, ובנוסף לכך אחד מהתנאים שהזכרתי קודם לא מתרחש - אני דרשתי מ-{% equation %}f\left(x\right){% endequation %} להיות חיובית בכל הקטע שעליו עושים אינטגרל, אבל זה לא קורה בשאלה למעלה.

בואו נסתכל על דוגמא אחרת - פונקציה שנראית כמו פרבולה, כמו בשאלה שלעיל, כך שיש לפרבולה חלק שבו היא נמצאת מתחת לציר {% equation %}x{% endequation %} (החלק בין הנקודות {% equation %}b{% endequation %} ו-{% equation %}c{% endequation %}):

<img src="{{site.baseurl}}{{site.post_images}}/2020/07/Integral2.PNG" alt=""/>

אני מסמן בתכלת את השטח שכלוא בין הפונקציה וציר {% equation %}x{% endequation %} בקטעים שבהם היא חיובית, ובירוק את השטח שכלוא בינה לבין ציר {% equation %}x{% endequation %} כשהיא שלילית. כדי לחשב את השטח הירוק, אני צריך לקחת את <strong>מינוס</strong> האינטגרל של הפונקציה בקטעים הללו. כלומר, השטח הכולל של ירוק + תכלת הולך להיות <strong>סכום</strong> של שלושה אינטגרלים מסויימים:

{% equation %}\int_{a}^{b}f\left(x\right)dx-\int_{b}^{c}f\left(x\right)dx+\int_{c}^{d}f\left(x\right)dx{% endequation %}

מה בעצם הרעיון פה? למה לוקחים את <strong>מינוס</strong> האינטגרל כדי לקבל את השטח הירוק? ובכן, כי האינטואיציה מאחורי אינטגרל מסויים היא לא "שטח" אלא "סכום", וכשהפונקציה שלילית, מה שקורה הוא שסוכמים הרבה ערכים שליליים ולכן הסכום שלהם יוצא שלילי. כדי לקבל שטח מתוך אינטגרל מסויים צריך לחשב את <strong>הערך המוחלט</strong> {% equation %}\int_{a}^{b}\left|f\left(x\right)\right|dx{% endequation %} והמשמעות של זה בפועל היא בדיוק מה שהצגתי - חלוקה לאיזורים חיוביים ושליליים ולקיחת מינוס האינטגרל עבור האיזורים השליליים.

ועכשיו אפשר להגיע אל המקרה <strong>הכללי ביותר והמועיל ביותר</strong>, שמדבר על הסיטואציה שבה יש לנו <strong>שתי פונקציות</strong> ואנחנו מחשבים את השטח שכלוא בין שתיהן ובין שני קווים אנכיים. זה נראה ככה:

<img src="{{site.baseurl}}{{site.post_images}}/2020/07/Integral3.PNG" alt=""/>

הסיטואציה היא זו: יש לנו שתי פונקציות {% equation %}f\left(x\right),g\left(x\right){% endequation %} כך ש-{% equation %}g\left(x\right)\le f\left(x\right){% endequation %} לכל {% equation %}a\le x\le b{% endequation %}. במקרה הזה אפשר להוכיח, כבר מההגדרה הבסיסית של אינטגרל מסויים (שאני לא מציג כאן...), שהשטח הירוק בתמונה שווה בדיוק ל-{% equation %}\int_{a}^{b}\left(f\left(x\right)-g\left(x\right)\right)dx{% endequation %}.

מה שנחמד בתוצאה הזו הוא ששתי התוצאות הקודמות שתיארתי נובעות ממנה: בשתי הדוגמאות הקודמות הפונקציה {% equation %}g\left(x\right){% endequation %} השתתפה בצורה סמויה - היא פשוט הייתה הפונקציה {% equation %}g\left(x\right)=0{% endequation %} הידועה גם בשם "ציר {% equation %}x{% endequation %}". כשחישבתי את {% equation %}\int_{a}^{b}f\left(x\right)dx{% endequation %} בעצם חישבתי את {% equation %}\int_{a}^{b}\left(f\left(x\right)-0\right)dx{% endequation %}, ולכן חישבתי את השטח שכלוא בין {% equation %}f{% endequation %} ובין {% equation %}g{% endequation %}, כלומר בין {% equation %}f{% endequation %} ובין ציר {% equation %}x{% endequation %}. במקרה שבו {% equation %}f\left(x\right)\le0{% endequation %} אז חישבתי בעצם את {% equation %}\int_{a}^{b}\left(0-f\left(x\right)\right)dx{% endequation %} ומכאן צץ המינוס.

זו בעצם התורה כולה - כל היתר הוא פשוט משחק ב"אילו שטחים אנחנו רוצים לחשב". בואו נראה את המשחק הזה עבור השאלה שאנחנו רוצים לפתור:

<img src="{{site.baseurl}}{{site.post_images}}/2020/07/Integral4.PNG" alt=""/>

השטח הירוק שבתמונה <strong>לא</strong> מתאים לתיאורים שנתתי עד כה, בגלל הצורה המורכבת שלו. החלק <strong>התחתון</strong> שלו הוא כל הזמן הפונקציה {% equation %}f\left(x\right){% endequation %}, אבל החלק <strong>העליון</strong> שלו מתחיל בתור קו אופקי, ואז פתאום הופך להיות הפונקציה {% equation %}g\left(x\right){% endequation %}. אז מה שנעשה יהיה למתוח קווים אנכיים, שאסמן בצבע כחול, בכל הנקודות המעניינות - תחילת וסוף השטח הירוק, והנקודה שבה החלק העליון של השטח משתנה:

<img src="{{site.baseurl}}{{site.post_images}}/2020/07/Integral5.PNG" alt=""/>

בשביל לפתור את התרגיל, נצטרך את הדברים הבאים:

<ul> <li>למצוא את המשוואה של הקו האופקי העליון (המשוואה היא בסך הכל {% equation %}h\left(x\right)=a{% endequation %} עבור {% equation %}a{% endequation %} קבוע כלשהו; האתגר הוא למצוא את {% equation %}a{% endequation %}).</li>


<li>למצוא את המשוואות של שלושת הקווים האנכיים הכחולים (שניים בעצם כבר מצאנו, כפי שאראה עוד רגע).</li>


<li>למצוא את האינטגרלים המסויימים עבור שני השטחים - הירוק והתכלת.</li>

</ul>

בואו ניזכר מה הפונקציות {% equation %}f,g{% endequation %} היו בעצם:

{% equation %}f\left(x\right)=x^{2}-6x+5{% endequation %}

{% equation %}g\left(x\right)=x^{2}-10x+21{% endequation %}

עכשיו, לישר האופקי: הוא עובר דרך הנקודה שבה {% equation %}f{% endequation %} חותכת את ציר {% equation %}y{% endequation %}, כלומר דרך הנקודה שהגובה שלה הוא {% equation %}f\left(0\right)=0^{2}-6\cdot0+5=5{% endequation %}. כלומר המשוואה של הישר הזה היא {% equation %}h\left(x\right)=5{% endequation %}. זה היה קל! עכשיו, לקווים האנכיים הכחולים. הראשון הוא בעצם הקו האנכי {% equation %}x=0{% endequation %}, מה שנקרא "ציר {% equation %}y{% endequation %}". ה<strong>שלישי</strong> עובר דרך נקודת החיתוך שמצאנו קודם - כלומר, הוא הקו {% equation %}x=4{% endequation %}. נשאר רק הקו האמצעי - הקו הזה עובר דרך נקודת החיתוך של הישר האופקי {% equation %}h\left(x\right)=5{% endequation %} עם הפונקציה {% equation %}g\left(x\right){% endequation %}, כלומר בנקודה {% equation %}x{% endequation %} שמקיימת {% equation %}g\left(x\right)=5{% endequation %}, כלומר בפתרון של המשוואה {% equation %}x^{2}-10x+21=5{% endequation %}, כלומר בפתרון של המשוואה {% equation %}x^{2}-10x+16=0{% endequation %}.

איך פותרים משוואה כזו? ובכן, אפשר עם נוסחת השורשים, אבל איפה הכיף פה? משהו שתמיד אפשר לעשות: לבדוק האם את המקדם החופשי, במקרה שלנו המספר 16, אפשר לכתוב בתור מכפלה של שני איברים שהסכום שלהם הוא <strong>מינוס</strong> המקדם האמצעי. במקרה שלנו, אפשר: {% equation %}16=2\cdot8{% endequation %}. אז נוקטים בתעלול הבא: מפרקים את המחובר האמצעי ומקבלים

{% equation %}x^{2}-2x-8x+16=0{% endequation %}

מוציאים גורמים משותפים ומקבלים

{% equation %}x\left(x-2\right)-8\left(x-2\right)=0{% endequation %}

ולבסוף:

{% equation %}\left(x-8\right)\left(x-2\right)=0{% endequation %}

זה בעצם אומר לנו שהפתרונות הם {% equation %}x=2,8{% endequation %}. אנחנו מחפשים את הפתרון הקטן יותר, שמתאים לנקודת החיתוך <strong>הראשונה</strong>, ולכן {% equation %}x=2{% endequation %} הוא מה שחיפשנו. בואו נוסיף לתמונה את כל המספרים שמצאנו:

<img src="{{site.baseurl}}{{site.post_images}}/2020/07/Integral6.PNG" alt=""/>

ועכשיו - לאינטגרלים! השטח הירוק כלוא בין הפונקציה {% equation %}h\left(x\right)=5{% endequation %} והפונקציה {% equation %}f\left(x\right){% endequation %} בקטע {% equation %}0\le x\le2{% endequation %} ולכן הוא שווה ל-

{% equation %}\int_{0}^{2}\left[5-\left(x^{2}-6x+5\right)\right]dx=\int_{0}^{2}\left(6x-x^{2}\right)dx{% endequation %}

האינטגרל הלא מסויים של {% equation %}6x-x^{2}{% endequation %} הוא {% equation %}3x^{2}-\frac{x^{3}}{3}{% endequation %}, מכללי האינטגרלים שכבר ראינו. אם מציבים בזה 0 מקבלים 0, ולכן הערך שאנחנו מחפשים הוא מה שקורה כשמציבים בכל זה 2: 

{% equation %}3\cdot2^{2}-\frac{2^{3}}{3}=12-\frac{8}{3}=\frac{36-8}{3}=\frac{28}{3}=9\frac{1}{3}{% endequation %}

עכשיו נעבור אל שטח התכלת: זה השטח שכלוא בין {% equation %}g\left(x\right){% endequation %} (מלמעלה) ו-{% equation %}f\left(x\right){% endequation %} (מלמטה) בקטע {% equation %}2\le x\le4{% endequation %}, ולכן:

{% equation %}\int_{2}^{4}\left(g\left(x\right)-f\left(x\right)\right)dx=\int_{2}^{4}\left[\left(x^{2}-10x+21\right)-\left(x^{2}-6x+5\right)\right]dx={% endequation %}

{% equation %}=\int_{2}^{4}\left(16-4x\right)dx{% endequation %}

האינטגרל הלא מסויים שלנו הפעם הוא {% equation %}16x-2x^{2}{% endequation %}, וכשמציבים {% equation %}4{% endequation %} ו-{% equation %}2{% endequation %} ומחסרים, מקבלים:

{% equation %}\left(16\cdot4-2\cdot4^{2}\right)-\left(16\cdot2-2\cdot2^{2}\right)=64-32-32+8=8{% endequation %}

נוסיף לזה את ה-{% equation %}9\frac{1}{3}{% endequation %} שחישבנו קודם, <strong>והפתרון לתרגיל כולו </strong>הוא {% equation %}17\frac{1}{3}{% endequation %}.

<h2>עצירת ביניים כדי לראות מה עשינו עד כה</h2>

ובכן, מה למדנו פה? אני מרגיש שבעצם כל מה שעשינו אי פעם מאז תחילת היקום היה לצייר שטחים בכל מני צבעים, אבל למעשה עברנו כברת דרך לא רעה להבנת "איך פותרים דברים עם אינטגרלים". הנה תקציר:

<ol> <li>ראינו שאינטגרל לא מסויים הוא "ההפך מנגזרת" ואיך בדיוק לחשב אותו עבור כל פולינום אפשרי (חוץ מ-{% equation %}x^{-1}{% endequation %} המעצבן הזה).</li>


<li>ראינו שאינטגרל מסויים קשור לאינטגרל לא מסויים בעזרת הנוסחה הקסומה {% equation %}\int_{a}^{b}f\left(x\right)dx=F\left(b\right)-F\left(a\right){% endequation %}</li>


<li>ראינו שאפשר להשתמש באינטגרל מסויים כדי לחשב שטחים שכלואים בצורה נחמדה בין שתי פונקציות ושני קווים מאונכים.</li>


<li>ראינו איך אפשר לחשב שטחים שכלואים בצורות מסובכות יותר על ידי פירוק שלהם לתת-שטחים שקל יותר לחשב וחיבור בהתאם.</li>

</ol>

רוב התרגיל שפתרנו היה בכלל תרגיל של מציאת נקודות חיתוך של פונקציות עם צירים - ובמקרה הזה, הטכניקה הייתה פתרון משוואות ממעלה שניה, שהיא כלי בסיסי (וחשוב!) באופן כללי. האינטגרלים באו כמעט כלאחר יד, אבל ככה זה תמיד פה - כאמור, אינטגרלים אמיתיים זה <strong>קשה</strong>, ולכן תרגילים על אינטגרלים לרוב מתבססים על משהו קל בהרבה.

אבל עדיין, מה עוד אנחנו יכולים לומר על חישוב אינטגרלים לא מסויימים?

<h2>פרק שלישי ובו עוד כמה אינטגרלים לא מסויימים</h2>

במתמטיקה יש כמה פונקציות נפוצות שטרם הזכרתי - סינוס, קוסינוס, טנגנס אקספוננט ולוגריתם. הן כל כך נפוצות שהן מופיעות בדף הנוסחאות עבור נגזרות, אז אני אזכיר מה מקבלים מהנגזרת שלהן - וננסה להבין מזה מה אנחנו יכולים לומר על אינטגרלים.

<ul> <li>{% equation %}\left(\sin x\right)^{\prime}=\cos x{% endequation %} מלמד אותנו ש-{% equation %}\int\cos xdx=\sin x+C{% endequation %}</li>


<li>{% equation %}\left(\cos x\right)^{\prime}=-\sin x{% endequation %} מלמד אותנו ש-{% equation %}\int\sin xdx=-\cos x+C{% endequation %}</li>


<li>{% equation %}\left(\tan x\right)^{\prime}=\frac{1}{\cos^{2}x}{% endequation %} מלמד אותנו ש-{% equation %}\int\frac{1}{\cos^{2}x}dx=\tan x+C{% endequation %}</li>


<li>{% equation %}\left(a^{x}\right)^{\prime}=a^{x}\cdot\ln a{% endequation %} מלמד אותנו ש-{% equation %}\int a^{x}dx=\frac{a^{x}}{\ln a}+C{% endequation %}</li>


<li>{% equation %}\left(\log_{a}x\right)^{\prime}=\frac{1}{x\ln a}{% endequation %} מלמד אותנו ש-{% equation %}\int\frac{1}{x}dx=\ln a\cdot\ln_{a}x+C{% endequation %}</li>

</ul>

את כל אלו אנחנו מסיקים ישר מדף הנוסחאות וממה שכבר למדנו על חישוב אינטגרלים לא מסויימים. אבל אני רוצה להתעכב שניה על שני האחרונים. ראשית, מה זה {% equation %}\ln{% endequation %}? זה מקרה פרטי של לוגריתם (<a href="https://gadial.net/2020/06/08/what_are_logarithms/">בדיוק כתבתי פוסט</a> על לוגריתמים!) שבו הבסיס הוא מספר מיוחד שמסומן {% equation %}e=2.7182\ldots{% endequation %}. נוסאות הגזירה מראות לנו בדיוק למה {% equation %}e{% endequation %} הזה הוא כל כך מיוחד שטורחים לתת לו שם: מכיוון ש-{% equation %}\ln x=\log_{e}x{% endequation %} אז {% equation %}\ln e=1{% endequation %} ולכן {% equation %}\left(e^{x}\right)^{\prime}=e^{x}{% endequation %}. כלומר, מבין כל הבסיסים האפשריים לפונקציית האקספוננט {% equation %}f\left(x\right)=a^{x}{% endequation %}, הבסיס {% equation %}e{% endequation %} הוא היחיד שעבורו גזירה של הפונקציה <strong>לא משנה אותה</strong>. לכן האינטגרל של הפונקציה הזו הוא פשוט במיוחד: {% equation %}\int e^{x}dx=e^{x}+C{% endequation %}.

באופן דומה, אפשר לקחת את נוסחת הגזירה של לוגריתם, שעובדת לכל בסיס {% equation %}a>1{% endequation %}, ולהשתמש בה עבור {% equation %}e{% endequation %} כדי לקבל {% equation %}\left(\ln x\right)^{\prime}=\frac{1}{x}{% endequation %}, ולכן לקבל את האינטגרל {% equation %}\int x^{-1}dx=\ln x+C{% endequation %}. זה מטפל <strong>סוף כל סוף</strong> גם ב-{% equation %}x^{-1}{% endequation %} שלא ידענו מה לעשות איתו עד כה; למעשה, זה טיפול כל כך טוב שלפעמים <strong>מגדירים</strong> את פונקציית הלוגריתם בעזרת האינטגרל הזה (עם עוד עניינים טכניים שלא אכנס אליהם). רק שימו לב שלוגריתם לא מוגדר בכלל עבור מספרים לא חיוביים, ולכן גם הנוסחה {% equation %}\int x^{-1}dx=\ln x+C{% endequation %} לא נכונה לכל מספר אלא רק עבור {% equation %}x>0{% endequation %}.

דף הנוסחאות מלמד אותנו עוד משהו על נגזרות, שנקרא <strong>כלל השרשרת</strong> אבל לא מצוין בשם הזה שם במפורש אלא נקרא "נגזרת של פונקציה מורכבת". הוא אומר:

{% equation %}\left[f\left(u\left(x\right)\right)\right]^{\prime}=f^{\prime}\left(u\right)\cdot u^{\prime}\left(x\right){% endequation %}

ואת זה הכי קל להסביר עם דוגמא. נאמר ש-{% equation %}f\left(t\right)=\cos t{% endequation %} וש-{% equation %}u\left(x\right)=x^{2}+3x{% endequation %}, ועכשיו אני תוקע את {% equation %}u\left(x\right){% endequation %} במקום {% equation %}t{% endequation %} , כלומר אני מקבל את הפונקציה המורכבת

{% equation %}\cos\left(x^{2}+3x\right){% endequation %}

ואת הפונקציה הזו אני גוזר על פי {% equation %}x{% endequation %}. אז כדי לקבל את התוצאה, אני עושה שני דברים:

<ul> <li>גוזר את {% equation %}f\left(t\right)=\cos t{% endequation %} על פי {% equation %}t{% endequation %}, ומקבל {% equation %}f^{\prime}\left(t\right)=-\sin t{% endequation %}</li>


<li>גוזר את {% equation %}u\left(x\right)=x^{2}+3x{% endequation %} על פי {% equation %}x{% endequation %} ומקבל {% equation %}u^{\prime}\left(x\right)=2x+3{% endequation %}</li>

</ul>

עכשיו, אני לוקח את {% equation %}f^{\prime}\left(t\right){% endequation %} שקיבלת בשלב הראשון ומציב בו את {% equation %}u\left(x\right)=x^{2}+3x{% endequation %} <strong>בלי שום שינוי</strong>, כלומר אני מקבל {% equation %}-\sin\left(x^{2}+3x\right){% endequation %}. את זה אני כופל ב-{% equation %}u^{\prime}\left(x\right){% endequation %} מהשלב השני, ובסך הכל אני מקבל:

{% equation %}-\sin\left(x^{2}+3x\right)\left(2x+3\right){% endequation %}

זה הרעיון מאחורי שימוש בכלל השרשרת, והמשמעות היא שאם נזהרים מספיק אפשר גם "להפוך" אותו כשעושים אינטגרל. מעשית, אם {% equation %}F^{\prime}\left(x\right)=f\left(x\right){% endequation %} ו-{% equation %}u\left(x\right){% endequation %} היא פונקציה כלשהי, אז:

{% equation %}F^{\prime}\left(u\left(x\right)\right)=f\left(u\left(x\right)\right)u^{\prime}\left(x\right){% endequation %}

כי זה כלל השרשרת בפעולה, ולכן:

{% equation %}\int f\left(u\left(x\right)\right)u^{\prime}\left(x\right)dx=F\left(u\left(x\right)\right)+C{% endequation %}

זה מופיע בדף הנוסחאות, אבל להשתמש בזה בפועל - זה יכול להיות מאוד טריקי, כי כשיש ביטוי חשבוני צריך איכשהו לזהות שהוא מורכבת מנגזרת של משהו, כפול המשהו המקורי כשהוא תקוע בתוך פונקציה אחרת. זה לא קל. לכן אני מנחש שאין הרבה תרגילים שמתבססים על זה, אבל אולי אני טועה?

בדף הנוסחאות יש גם מקרה פרטי פשוט במיוחד של הסיפור הזה: כש-{% equation %}u\left(x\right)=mx+b{% endequation %} (זה פשוט פולינום ממעלה ראשונה) אז {% equation %}u^{\prime}=m{% endequation %} ולכן {% equation %}F^{\prime}\left(mx+b\right)=f\left(mx+b\right)\cdot m{% endequation %} (זה כלל השרשרת בפעולה שוב), ולכן כשעוברים לאינטגרל, מקבלים {% equation %}\int f\left(mx+b\right)dx=\frac{1}{m}F\left(mx+b\right)+C{% endequation %}.

וזהו, אלו כל הנוסחאות שקשורות לאינטגרלים בדף הנוסחאות. מקווה שעכשיו הן קצת יותר ברורות ויותר קל להבין איך לחשב אינטגרלים לא מסויימים.

בעולם "האמיתי", כאן רק מתחיל הסיפור; יש עוד המון נוסחאות של אינטגרלים בסיסיים; יש שיטות אינטגרציה נחמדות שעוזרות לפתור מקרים יותר מסובכים, כמו למשל <strong>אינטגרציה בחלקים</strong> שמבוססת על החוק עבור נגזרת של מכפלה, שלא הצגתי פה. ויש פונקציות שפשוט <strong>לא קיים</strong> להן אינטגרל לא מסויים שאפשר להציג בצורה פשוטה בעזרת פונקציות אלמנטריות. למשל הפונקציה {% equation %}e^{x^{2}}{% endequation %}.

<h2>פרק רביעי ובו אנו מסיימים בנימה אופטימית עם תרגיל מבגרות שכל מה שלמדנו לא עוזר בו בכלל</h2>

לסיום, אני רוצה להראות תרגיל מבגרות של השנה:

<img src="{{site.baseurl}}{{site.post_images}}/2020/07/IntegralQuestion2.PNG" alt=""/>

השאלה הזו היא <strong>קצת</strong> יותר מתוחכמת מהסטנדרט, אבל יש פיצוי הולם על כך - רובה מתבסס על לתת הנחיה גדולה מה בעצם לעשות. השאלה היא בעצם זו: אם {% equation %}f\left(x\right)=e^{x}\left(x-5\right){% endequation %}, מהו {% equation %}\int f\left(x\right)dx{% endequation %}? זו לבדה שאלה די טריקית - הרי {% equation %}e^{x}\left(x-5\right){% endequation %} היא פונקציה מסובכת - מכפלה של שתי פונקציות שלא נראית כמו אף אחת מנוסחאות האינטגרלים שאנחנו מכירים. הדבר היחיד עם מכפלה שראינו היה הנוסחה שקשורה לכלל השרשרת, אבל לא נראה שאפשר להשתמש בה כאן. אז מה עושים?

בעולם האמיתי משתמשים במה שנקרא "אינטגרציה בחלקים", אבל זה לא אפשרי כאן. אז מה שקורה כאן הוא ש<strong>נותנים לתלמידים את הפתרון על מגש של כסף</strong>; הסעיפים הראשונים בשאלה אמורים להנחות את התלמידים אל עבר הפתרון.

ראשית, למה הנגזרת של {% equation %}f{% endequation %} יוצאת מה שהיא יוצאת? בשביל זה צריך להיזכר במפורש במה שקורה כשגוזרים <strong>מכפלה</strong> של פונקציות. אם {% equation %}f\left(x\right)=g\left(x\right)h\left(x\right){% endequation %} אז

{% equation %}f^{\prime}\left(x\right)=g^{\prime}\left(x\right)h\left(x\right)+g\left(x\right)h^{\prime}\left(x\right){% endequation %}

כלומר, גוזרים כל אחת מהפונקציות במכפלה בנפרד וכופלים אותה בפונקציה השניה <strong>הלא גזורה</strong> ומחברים. במקרה שלנו {% equation %}g\left(x\right)=e^{x}{% endequation %} שהיא פשוטה במיוחד כי {% equation %}g^{\prime}\left(x\right)=e^{x}{% endequation %} גם כן, ואילו {% equation %}h\left(x\right)=x-5{% endequation %} ולכן {% equation %}h^{\prime}\left(x\right)=1{% endequation %}, ונקבל:

{% equation %}f^{\prime}\left(x\right)=e^{x}\left(x-5\right)+e^{x}\cdot1=e^{x}\left(x-5+1\right)=e^{x}\left(x-4\right){% endequation %}

שימו לב שהמספר 5 לא באמת שיחק תפקיד בנגזרות, ולכן אותו דבר קורה גם כשגוזרים שוב ושוב - בכל פעם הערך שמפחיתים מ-{% equation %}x{% endequation %} הולך <strong>וקטן</strong>. התרגיל <strong>נותן במפורש את החוקיות הכללית</strong> של הנגזרת ומבקש מהתלמידים לוודא אותה.

אז מה עושים בסעיף ד'? צריך להבין שאפשר לקחת את החוקיות הזו וללכת איתה גם <strong>צעד אחד אחורה</strong>. כלומר, במקום שהמספר שמחסרים מ-{% equation %}x{% endequation %} <strong>יקטן </strong>ב-1, הוא צריך <strong>לגדול</strong> ב-1. כלומר, {% equation %}F\left(x\right)=e^{x}\left(x-6\right){% endequation %}. אם נגזור את {% equation %}F\left(x\right){% endequation %} נראה שזה עובד.

אבל רגע, שניה, לא סיימנו. מה שהמבחן בודק הוא שהתלמידים באמת מבינים את הרעיון של אינטגרל לא מסויים עד הסוף - בפרט, את זה שלאותה פונקציה {% equation %}f{% endequation %} יש <strong>אינסוף</strong> פונקציות קדומות אפשריות. המבחן דורש בצורה מפורשת שמבין האינסוף הללו, ניתן את זו שעוברת <strong>בראשית הצירים</strong>. המשמעות היא שאנחנו צריכים למצוא {% equation %}F{% endequation %} כזו שמקיימת {% equation %}F\left(0\right)=0{% endequation %}.

כמובן, קל לעשות את זה: הצורה הכללית של פונקציה קדומה שכזו היא {% equation %}F\left(x\right)=e^{x}\left(x-6\right)+C{% endequation %}. אם נציב {% equation %}x=0{% endequation %} נקבל את המשוואה {% equation %}e^{0}\left(0-6\right)+C=0{% endequation %}, כלומר {% equation %}C=6{% endequation %}. לכן הפונקציה הקדומה שאנחנו מחפשים היא {% equation %}F\left(x\right)=e^{x}\left(x-6\right)+6{% endequation %}, וסיימנו.

האם זה מסיים את סיפור האינטגרלים? ובכן, אני משער שיש עוד הרבה סוגי שאלות שלא לגמרי כיסיתי פה. אתן מוזמנות להפגיז איתן בתגובות ואולי אכתוב פוסט המשך. 