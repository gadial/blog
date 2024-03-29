---
id: 222
title: "חידת מעטפות"
date: 2009-12-31 11:39:19
layout: post
categories: 
  - הסתברות
  - משחקים וחידות מתמטיות
tags: 
  - תוצאות לא אינטואיטיביות
---
לכבוד סוף השנה, חידה: אתם נמצאים בחדר שבו נמצאות שתי מעטפות, כל אחת עם סכום כסף שנבחר באקראי (לדקדקנים - נבחר מתוך התפלגות כלשהי על המספרים הממשיים - לא ידוע לכם איזו התפלגות). אתם בוחרים באקראי (כלומר, בהסתברות 50:50) את אחת המעטפות, פותחים אותה ורואים את הסכום שבפנים. כעת מאתגרים אתכם - החליטו אם להחליף או לא. המטרה: למצוא שיטת החלטה שבה מובטח שבהסתברות של יותר מ-{% equation %}\frac{1}{2}{% endequation %} תסיימו עם הסכום הגדול יותר מבין השניים. מה עושים?

ייתכן שחלקכם אומרים "אה, זה בדיוק <a href="http://www.gadial.net/2008/07/25/envelope_paradox/">פרדוקס המעטפות</a>! אז כדאי תמיד להחליף!" אלא שזה לא בדיוק כך. פרדוקס המעטפות עובד עבור מעטפות שהסכומים בהם הוגרלו על ידי התפלגויות מסויימות, שצריך "להנדס" כדי שיתאימו לפרדוקס (הרחבתי על כך בפוסט המתאים) - ויותר מכך, הסיבה שבגללה תמיד כדאי להחליף עבור אותן התפלגויות נובעת משיקולי תוחלת הרווח של ההחלפה; הטיעון הבסיסי הוא "אם אני מחליף וגומר עם המעטפה בעלת הסכום הגדול יותר, אני ארוויח הרבה יותר משאפסיד אם אגמור עם המעטפה בעלת הסכום הקטן יותר". כאן לא נדרש מאיתנו להרוויח כסף בתוחלת, אלא פשוט לסיים עם המעטפה בעלת הסכום הגבוה יותר, בהסתברות גבוהה מחצי.

למעשה, שיטת הפעולה של "תחליף תמיד" בבירור לא תיתן הסתברות גבוהה מחצי; אם מלכתחילה בחרנו את המעטפה בעלת הסכום הגבוה יותר (בהסתברות {% equation %}\frac{1}{2}{% endequation %}), אז נפסיד, ואחרת (גם כן בהסתברות {% equation %}\frac{1}{2}{% endequation %}) ננצח. אם כן, יש לנו כאן חידה ששונה מהותית מפרדוקס המעטפות - ועל פניו לא ברור אם היא פתירה בכלל. קחו עכשיו מספר דקות וחשבו על החידה - לאחר מכן אנסה להציג שני פתרונות שונים עבורה.

האתגר שהחידה הזו מציבה נעוץ בכך שאין לנו מושג אילו סכומים נמצאים במעטפות ועל פי מה נקבע איך הם הגיעו לשם. אנחנו צריכים שיטה שתהיה טובה באופן כללי, לכל זוג אפשרי של מספרים {% equation %}a,b{% endequation %} שיכולים להיות במעטפות. נבחר את הסימונים לשני הסכומים הללו כך ש-{% equation %}a{% endequation %} הוא הקטן יותר, כלומר {% equation %}a\le b{% endequation %}. השאלה הראשונה, אם כן, היא מה בעצם ידוע לי ובמה אני יכול להשתמש.

ובכן, כל מה שידוע לי הוא הערך שנמצא במעטפה שפתחתי, אותו אסמן ב-{% equation %}x{% endequation %}. כלל ההחלטה שלי ניתן יהיה לתיאור באופן כללי בתור פונקציה {% equation %}f\left(x\right){% endequation %} שלכל {% equation %}x{% endequation %} מתאימה את ההסתברות שאבחר לא להחליף. עד כאן פורמליסטיקה, וכעת נפנה לפתרון כלשהו. האינטואיציה הראשונה שלי בתרגיל הזה היא שככל ש-{% equation %}x{% endequation %} גדול יותר, כך אני אתפתה <strong>פחות</strong> להחליף אותו. הדרך הפורמלית לבצע משהו כזה היא לבחור בתור {% equation %}f{% endequation %} פונקציה שעולה תמיד (כלומר, אם {% equation %}x&lt;y{% endequation %} אז {% equation %}f\left(x\right)&lt;f\left(y\right){% endequation %}) ועם זאת ערכיה נמצאים כל הזמן בתוך התחום {% equation %}\left[0,1\right]{% endequation %} (אחרת היא לא מייצגת הסתברות). לא קשה לבנות פונקציות כאלו - למשל באמצעות מניפולציה על הפונקציה {% equation %}\arctan{% endequation %} (הפונקציה ההופכית לטנגנס) - זוהי פונקציה עולה ממש שערכיה נעים בתחום {% equation %}\left[-\pi/2,\pi/2\right]{% endequation %}, כך שרק צריך "לכווץ" אותה מעט ו"להרים" אותה מעט כדי לקבל {% equation %}f{% endequation %} כמו שרציתי. ברשותכם אפסח על הפרטים הטכניים הללו.

ובכן, מסתבר ש-{% equation %}f{% endequation %} שכזו עובדת מצויין. בואו נחשב את ההסתברות שאנצח, אם אני נעזר ב-{% equation %}f{% endequation %} הזו. ההסתברות שאנצח היא ההסתברות שאבחר בהתחלה את {% equation %}a{% endequation %} (בהסתברות חצי) ואז בגלל {% equation %}f{% endequation %} אבחר להחליף (בהסתברות {% equation %}1-f\left(a\right){% endequation %}), ועוד ההסתברות שאבחר בהתחלה את {% equation %}b{% endequation %} (שוב, בהסתברות חצי) ואז בגלל {% equation %}f{% endequation %} אבחר דווקא לא להחליף (בהסתברות {% equation %}f\left(b\right){% endequation %}). מה ההסתברות שלי לנצח? {% equation %}\frac{1}{2}\cdot\left(1-f\left(a\right)\right)+\frac{1}{2}\cdot f\left(b\right)=\frac{1}{2}\left(1+f\left(b\right)-f\left(a\right)\right)=\frac{1}{2}+\frac{1}{2}\left(f\left(b\right)-f\left(a\right)\right){% endequation %}, והסתברות זו גדולה ממש מחצי כאשר {% equation %}a&lt;b{% endequation %}, כי אז {% equation %}f\left(a\right)&lt;f\left(b\right){% endequation %}, כלומר {% equation %}f\left(b\right)-f\left(a\right)&gt;0{% endequation %} (אם {% equation %}a=b{% endequation %} אז אני מנצח תמיד, כי לא משנה מה אעשה - אסיים עם הסכום הגדול מבין השניים, שבמקרה זה הם שווים).

כעת אני רוצה להציג דרך אחרת לפתרון, שהמעניין בה היא שהיא אינה קונסטרוקטיבית במיוחד - למעשה, האסטרטגיה שהיא מציעה יכולה להיות מעורפלת כמעט כמו שיטת בחירת הכסף למעטפות. הרעיון פשוט: בחר באקראי מספר ממשי, כשהדרישה היחידה היא שכל מספר ממשי יכול להיבחר (פורמלית - פונקצית צפיפות ההסתברות של ההגרלה צריכה להיות חיובית תמיד) והשווה אותו ל-{% equation %}x{% endequation %} שראית במעטפה שלך. אם המספר שהגרלת גדול יותר, תחליף; אחרת, תישאר.

מה קורה כאן? צריך להבדיל בין שלושה מקרים אפשריים, לפי הזהות של המספר שהגרלתי, שאסמנו {% equation %}y{% endequation %}. אם {% equation %}y\le a&lt;b{% endequation %}, אז לא משנה מה נמצא במעטפה שפתחתי, אני לא הולך להחליף; לכן ההסתברות שלי להצליח היא בדיוק חצי. באופן דומה, אם {% equation %}a&lt;b&lt;y{% endequation %} אז לא משנה מה נמצא במעטפה שפתחתי, כן אחליף, ולכן שוב ההסתברות שלי להצליח היא חצי. האקשן מתחיל כאשר {% equation %}a&lt;y\le b{% endequation %}; במקרה זה <strong>תמיד אנצח</strong>. לא משנה אם ראיתי את {% equation %}a{% endequation %} או {% equation %}b{% endequation %}. אם ראיתי את {% equation %}a{% endequation %}, אז ה-{% equation %}y{% endequation %} שהגרלתי גדול יותר ממנו, ולכן אחליף ואנצח; ואם ראיתי את {% equation %}b{% endequation %} אז ה-{% equation %}y{% endequation %} שלי קטן יותר ממנו ולכן לא אחליף ואנצח.

הבה ונעשה כעת את החישוב הפורמלי. אנחנו צריכים להבדיל בין ההסתברות של שלושה מקרים: {% equation %}P\left(y\le a\right),P\left(y&gt;b\right),P\left(a&lt;y\le b\right){% endequation %}. אלו שלושת המקרים האפשריים היחידים, ולכן סכום ההסתברויות שלהם הוא 1, וכדי לחשב את ההסתברות שאנצח צריך לכפול כל אחד מהם בהסתברות לנצח בהניתן שהוא קרה. נקבל את הסכום הבא:

{% equation %}\frac{1}{2}P\left(y\le a\right)+\frac{1}{2}P\left(y&gt;b\right)+P\left(a&lt;y\le b\right){% endequation %}

{% equation %}= \frac{1}{2}\left(P\left(y\le a\right)+P\left(y&gt;b\right)+P\left(a&lt;y\le b\right)\right)+\frac{1}{2}P\left(a&lt;y\le b\right){% endequation %}
{% equation %}= \frac{1}{2}+\frac{1}{2}P\left(a&lt;y\le b\right){% endequation %}

אם כן, שוב קיבלתי הסתברות הצלחה של "חצי ועוד קצת". כל מה שנדרש ממני הוא שההתפלגות שבה אני בוחר את {% equation %}y{% endequation %} תהיה כזו שבה לכל {% equation %}a&lt;b{% endequation %}, ההסתברות שיתקיים {% equation %}a&lt;y\le b{% endequation %} תהיה חיובית. התפלגות נורמלית היא הדוגמה הקלאסית להתפלגות שבה זה מתקיים, אך כאמור - כל התפלגות עם פונקצית צפיפות הסתברות חיובית תמיד עובדת (ואין בעיה גם עם פונקציות מוגבלות יותר, עם נקודות אי רציפות סליקות - אבל למה לחפור בכך?)

שני הפתרונות מקסימים לטעמי, והתוצאה של החידה הזו היא אנטי-אינטואיטיבית בעליל. מסתבר שבמתמטיקה, גם כשאתה לא יודע כלום, אתה יכול לדעת משהו.
