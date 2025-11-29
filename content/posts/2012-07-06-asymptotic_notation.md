---
id: 2054
title: "הסבר בזמן (O(n על סימונים אסימפטוטיים"
date: 2012-07-06 12:19:48
layout: post
categories: 
  - מבני נתונים ואלגוריתמים
  - תכנות
tags: 
  - אלגוריתמים
  - סיבוכיות
  - סימון אסימפטוטי
  - סימונים מתמטיים
---


<p>כל מי שמתחיל ללמוד מדעי המחשב נתקל חיש קל בסימון האסימפטוטי {% equation %}O\left(n\right){% endequation %}. המשפט הזה נשמע לכם כמו ג'יבריש מוחלט? מצויין! הפוסט הזה מיועד בעיקר לכם, ובפרט לאלו מכם שהעניין הזה הבהיל אותם מלהתעסק במדעי המחשב. השורה התחתונה היא שזה סימון מתמטי פשוט יחסית, שמטרתו לעשות את החיים <strong>קלים</strong> לכל העוסקים במלאכה; בואו ננסה להבין למה בכלל צריך לעשות את החיים קלים, ואיך הסימון הזה עושה אותם כאלה.</p>

<p>נתחיל בניתוץ המיתוס הבסיסי. אנשים מגיעים משום מה למסקנה שמתמטיקאים הם אנשים מאוד מדויקים, ושהם אנשים מאוד חרוצים. לא נכון! מתמטיקאים הם עצלנים והם מאוד אוהבים קירובים והזנחות. הם פשוט עושים אותם <strong>נכון</strong>. בעוד שהפיזיקאי יגיד "הממ... עבור ערכים קרובים לאפס של {% equation %}x{% endequation %} מתקיים ש-{% equation %}x{% endequation %} ו-{% equation %}\sin x{% endequation %} זה בערך אותו דבר" ואז יחליף כל מופע במשוואה של {% equation %}\sin x{% endequation %} ל-{% equation %}x{% endequation %}, המתמטיקאי יגיד "הממ, כאשר {% equation %}x\to0{% endequation %} אז {% equation %}\sin x=x+o\left(1\right){% endequation %}". המטרה היא לתת למשוואה השניה משמעות מדויקת ופורמלית, למרות שהיא מתארת קירוב והזנחה.</p>

<p>במדעי המחשב קירובים שכאלו הופכים להיות צורך אקוטי למדי. חלק ניכר מהמתמטיקה של מדעי המחשב עוסקת בניתוח זמן הריצה של אלגוריתמים (מהו אלגוריתם? חשבו עליו כעל תוכנית מחשב. מהי תוכנית מחשב? אה...). עכשיו, אפילו אלגוריתמים פשוטים הם עדיין בעייתיים לניתוח מדויק. ראשית כל צריך להגדיר מהו "צעד בסיסי" שהאלגוריתם מבצע, וזה כבר אסון: האם פעולה חשבונית היא צעד בסיסי? אבל אנו יודעים שחיבור לוקח זמן קצר בהרבה מאשר כפל או, חס ושלום, חילוק. אבל מצד שני, במחשבים שבהם מספרים מיוצגים בצורה סטנדרטית, כפל או חלוקה ב-2 הם דווקא קלים מאוד לביצוע על ידי הזזה של ביט בודד; ברמת החומרה אפשר אולי לממש את זה אפילו יותר מהר מאשר חיבור! בנוסף, הזמן שדורשות פעולות בסיסיות עשוי להשתנות ממעבד למעבד; הוא עשוי להיות תלוי בתנאים הפיזיים שבהם המעבד פועל באותו הרגע; והאלגוריתם עצמו עשוי לרוץ על מעבד שמבצע אופטימיזציות מתוחכמות (למשל Brach prediction או Out-of-order execution). בקיצור, כאשר מנתחים את זמן הריצה של אלגוריתמים, מראש ברור לכולם שאנחנו לא יכולים לקבל מספר מדויק אלא רק הערכה; לכן השימוש בקירובים הוא כל כך טבעי.</p>

<p>מכיוון שאין משמעות למספרים מדוייקים, מה שאנחנו רוצים לדעת הוא את <strong>ההתנהגות האסימפטוטית של זמן הריצה</strong>. מה זה אומר? בדרך כלל אלגוריתם נבנה כך שיהיה מסוגל לעבוד על קלטים מכל גודל שהוא. אז אפשר לדבר על פונקציה {% equation %}f\left(n\right){% endequation %} שמקבלת את גודל הקלט (גם "גודל הקלט" הוא מושג שנתון לכמה פרשנויות) ומחזירה את זמן הריצה של האלגוריתם על אותו קלט, כאשר זמן הריצה הזה הוא פשוט "מספר הצעדים הבסיסיים" של האלגוריתם (זכרו - "צעד בסיסי" תלוי באלגוריתם עצמו ובמה שאנו מוכנים לקרוא לו צעד בסיסי; ובהחלט ייתכן ששתי פעולות שונות, שלוקחות פרק זמן שונה, עדיין יחשבו שתיהן ל"צעד בסיסי"). לחשב את {% equation %}f\left(n\right){% endequation %} בצורה מדויקת זה כאב ראש, אבל אפשר <strong>להשוות</strong> את {% equation %}f\left(n\right){% endequation %} לפונקציות פשוטות, למשל {% equation %}n^{2}{% endequation %}. אם למשל לכל {% equation %}n{% endequation %} טבעי מתקיים {% equation %}f\left(n\right)&lt;n^{2}{% endequation %}, אז אנחנו יודעים שזמן הריצה של האלגוריתם שמיוצג על ידי {% equation %}f{% endequation %} הוא לא גדול <strong>מדי</strong> - הוא לכל היותר ריבועי בגודל הקלט.</p>

<p>הבעיה היא שחסם כזה לעתים קרובות לא עובד. בואו נחשוב על תוכנית מחשב שמקבלת כקלט רשימה בעלת {% equation %}n{% endequation %} איברים שהם מספרים טבעיים, ומוצאת את את המספר המקסימלי והמינימלי ברשימה. הדרך הפשוטה לעשות זאת: לתחזק שני משתני עזר ששניהם מאותחלים להיות האיבר הראשון ברשימה; לאחר מכן לעבור סדרתית על הרשימה ולהשוות כל איבר ברשימה הן למקסימום והן למינימום הנוכחיים. אם האיבר החדש גדול מהמקסימום הנוכחי, משנים את המקסימום כך שישתווה לו; אם האיבר החדש קטן מהמינימום הנוכחי, משנים את המינימום כך שישתווה לו. בסיום המעבר על הרשימה המשתנים של המקסימום והמינימום יחזיקו את הערך הנכון. הנה פונקציה בשפת Ruby שעושה את זה:</p>

<div class="code-block">
{% highlight ruby %}
def find_min_max(list)
  min = max = list[0]
  for k in 1...list.length do
    min = list[k] if min > list[k]
    max = list[k] if max < list[k]
  end
  return [min, max]
end
{% endhighlight %}
</div>


<p>(למה רובי? כי זו אחת מהשפות הללו שבהן הקוד נראה פשוט כמעט כמו פסאודו-קוד ויש לו את היתרון שהוא גם עובד בפועל. אני לא בהכרח כותב בצורה שהכי מתאימה לרובי, כי המטרה היא ליצור קוד קריא גם למי שלא בקיאים בטריקים של השפה).</p>

<p>אז מה יש לנו כאן? שתי פעולות אתחול, ועוד {% equation %}2n-2{% endequation %} פעולות השוואה (כש-{% equation %}n{% endequation %} הוא הגודל של list) שאם כל אחת מהן מצליחה, יש לנו עוד פעולת השמה. במקרה הגרוע ביותר (שהוא מה שבדרך כלל אנו מתעניינים בו) כל פעולת השוואה "תצליח" ולכן תסתיים בהשמה, כך שיהיו לנו עוד {% equation %}2n-2{% endequation %} פעולות השמה (בפועל זה לא יכול לקרות אף פעם - למה?). סך הכל: {% equation %}4n-2{% endequation %} פעולות בסיסיות של השוואה והשמה. אז חסם עבור האלגוריתם הוא {% equation %}f\left(n\right)&lt;4n{% endequation %}, אבל בשביל מה צריך את ה-4 שם? אין לו חשיבות אסימפטוטית גדולה במיוחד, במובן זה שאפילו {% equation %}100n{% endequation %} זה עדיין יותר מהיר עבור ערכים גדולים של {% equation %}n{% endequation %} מאשר, נאמר, {% equation %}n^{2}{% endequation %}. חוץ מזה, בגלל שהשוואה והשמה לא לוקחות אותו פרק זמן, ה-4 הזה הוא ממילא שקר: אם, למשל, פעולה של השוואה לוקחת פי 2 יותר זמן מפעולה של השמה אז נכון לחשוב על השוואה כשתי פעולות בסיסיות ואז נקבל {% equation %}2n+2\left(2n-2\right)=6n-4{% endequation %} פעולות בסיסיות, כלומר חסם של {% equation %}f\left(n\right)&lt;6n{% endequation %} - שינוי בקבוע שבו מוכפל ה-{% equation %}n{% endequation %}. לכן אנחנו מעדיפים להשתמש בסימון שממילא לא מתעניין בקבועים הללו ולומר ש-{% equation %}f\left(n\right)=O\left(n\right){% endequation %}.</p>

<p>בהערת אגב, לפעמים כן רוצים לשפר את הקבועים למרות שזה לא יבוא לידי ביטוי בסימון האסימפטוטי. כדאי להבהיר את הנקודה הזו מראש. יש תעלול נחמד שחוסך בערך רבע מהבדיקות עבור מציאת המינימום והמקסימום - במקום לבדוק כל פעם את האיבר הבא במערך, בודקים את <strong>שני</strong> האיברים הבאים; קודם משווים אותם זה לזה, ואז משווים את הגדול שבהם למקסימום, והקטן שבהם למינימום. באופן הזה במקום לבצע 4 בדיקות במקרה הגרוע ביותר (2 עבור כל אחד משני האיברים) מבצעים רק 3. הנה הקוד:</p>

<div class="code-block">
{% highlight ruby %}
def faster_find_min_max(list)
  min = max = list[0]
  k = (list.length % 2 == 1)?(1):(0)

  while k < list.length
    if (list[k] < list[k+1])
      min_candidate, max_candidate = list[k], list[k+1]
    else
      min_candidate, max_candidate = list[k+1], list[k]
    end
    max = max_candidate if max_candidate > max
    min = min_candidate if min_candidate < min

    k = k + 2
  end

  return [min, max]
end
{% endhighlight %}
</div>

<p>שימו לב שהקוד מתחיל באיזו בדיקה האם הרשימה זוגית או אי זוגית באורכה כדי להמנע מחריגה מגבולות הרשימה לקראת הסוף. לכאורה כאן הוספתי עבודה ביחס לאלגוריתם הקודם, אבל זו בדיקה <strong>חד פעמית</strong> - הזמן שנדרש לבצע אותה לא תלוי באורך הרשימה, ולכן בדרך כלל אנחנו רק חוסכים כאן פעולות. החסכון לא נראה מהותי במיוחד כרגע, אבל באלגוריתמים כאלו תמיד צריך לזכור שבסופו של דבר התוכנית לא תרוץ בפני עצמה אלא בתור תת-תוכנית שבתוך תת-תוכנית שבתוך תת-תוכנית שבתוך תת-תוכנית של איזו תוכנית מורכבת שעושה חישובים מתוחכמים, ורצה על קלטים שהם רשימות שמכילות מיליוני איברים, ועושה את זה אלפי פעמים, כל הזמן. בסופו של דבר יש סיכוי טוב שקטע הקוד הקצרצר שלמעלה יהיה החלק העמוס ביותר בתוכנית שכוללת מיליוני שורות קוד, ושיפור כלשהו בקטע הקוד הזה - אפילו מינורי - יגרום לתוכנית לרוץ משמעותית מהר יותר.</p>

<p>עם זאת, חשוב לזכור שזה <strong>לרוב לא ככה</strong>. לא תמיד כדאי לכתוב קוד אופטימלי בכוח מלכתחילה (מה שעשוי לגרום לשגיאות רבות יותר או אפילו להיות איטי יותר בסיטואציות מסוימות). לרוב עדיף פשוט לכתוב קוד פשוט שעובד, ואחר כך, אם רואים שצוואר הבקבוק של התןכנית הוא בדיוק בקטע הקוד הזה, לשפר אותו (כמובן שיש סיטואציות שבהן <strong>ברור</strong> שתהיה בעיה עם קוד מסויים ואז כותבים את הגרסה האופטימלית שלו מראש - אין כללים מוחלטים כאן).</p>

<p>יפה. כל המבוא הזה בא לתת תחושה של למה צריך סימונים אסימפטוטיים. עכשיו בואו נסביר באופן מדויק מה הם אומרים.</p>

<p>ראשית כל, צריך להבהיר מה "שדה המשחק" שלנו. אנחנו מדברים על פונקציות {% equation %}f:\mathbb{N}\to\mathbb{N}{% endequation %} שמקבלות מספרים טבעיים ומחזירות מספרים טבעיים. אפשר לדבר על סימונים אסימפטוטיים גם בהקשרים אחרים ואתן דוגמאות לכך, אבל אז נצהיר במפורש על שינוי שדה המשחק. בניתוח סיבוכיות של אלגוריתמים פונקציות מטבעיים לטבעיים הן מה שצץ באופן טבעי, כי אורך קלט ומספר צעדי ריצה הם בדרך כלל מספרים טבעיים (אפשר להתקטנן כאן. בואו לא נעשה את זה).</p>

<p>הסימון הפופולרי ביותר הוא {% equation %}f\left(n\right)=O\left(g\left(n\right)\right){% endequation %} (קרי: "{% equation %}f{% endequation %} היא או-גדול של {% equation %}g{% endequation %}"), כאשר {% equation %}f\left(n\right),g\left(n\right){% endequation %} הן פונקציות כלשהן. את הסימון הזה יש לקרוא בתור "{% equation %}f\left(n\right){% endequation %} קטן או שווה אסימפטוטית ל-{% equation %}g\left(n\right){% endequation %}". פורמלית, זה אומר שקיים קבוע {% equation %}c>0{% endequation %} (שיכול להיות כל מספר ממשי) ומספר טבעי {% equation %}n_{0}{% endequation %} כך ש-{% equation %}f\left(n\right)&lt;c\cdot g\left(n\right){% endequation %} עבור כל {% equation %}n>n_{0}{% endequation %}. למי שבקיא בחשבון אינפיניטסימלי זה בוודאי קצת מזכיר את הגדרת הגבול; ואכן, אם {% equation %}\lim_{n\to\infty}\frac{f\left(n\right)}{g\left(n\right)}&lt;c{% endequation %} אז {% equation %}f\left(n\right)=O\left(g\left(n\right)\right){% endequation %} (אבל ההפך לא נכון כי לא מובטח שהגבול יהיה קיים).</p>

<p>ההגדרה הזו עושה שני דברים: ראשית, היא מתעלמת מקבועים, בכך שהיא מרשה ל-{% equation %}g\left(n\right){% endequation %} להיות מוכפל בקבוע כלשהו; שנית, היא מתעלמת מערכים קטנים של {% equation %}n{% endequation %} בכך שהיא מרשה לאי השוויון להתקיים רק החל מ-{% equation %}n_{0}{% endequation %} כלשהו. זה אומר שאנחנו מתעניינים רק ב"התנהגות לטווח ארוך" של הפונקציה, מה שכמובן פותח פתח לאנומליות של אלגוריתם א' שטוב יותר אסימפטוטית מאלגוריתם ב', אבל רק עבור קלטים שהגודל שלהם גדול ממספר האטומים ביקום. כן, זה קורה. כן, כל מדעני המחשב מודעים לזה. כן, זה לא מפריע לנו אם אנחנו לא מסיקים מחסמים אסימפטוטיים שכאלו יותר מאשר צריך להסיק מהם.</p>

<p>עד כאן הכל טוב. הבעיה היא שלפעמים רוצים להשתמש בסימון {% equation %}O{% endequation %} גם באגף שמאל של המשוואה, ואז All hell breaks loose. למשל, הביטו במשוואה הבאה:</p>

<p>{% equation %}n^{2}+O\left(n\right)=O\left(n^{2}\right){% endequation %}</p>

<p>המשוואה רוצה לומר את הדבר הבא - קחו את הפונקציה {% equation %}n^{2}{% endequation %} ותוסיפו לה פונקציה <strong>כלשהי</strong> {% equation %}h\left(n\right){% endequation %} שמקיימת {% equation %}h\left(n\right)=O\left(n\right){% endequation %}, והתוצאה הכוללת תהיה {% equation %}O\left(n^{2}\right){% endequation %}. במילים אחרות, משמעותו הפורמלית של השוויון שלמעלה היא "לכל {% equation %}h\left(n\right)=O\left(n\right){% endequation %} מתקיים {% equation %}n^{2}+h\left(n\right)=O\left(n^{2}\right){% endequation %}".</p>

<p>טוב ויפה, אבל כדי לראות איך זה מסתבך, שימו לב לכך שאפשר היה להיפטר לגמרי מה-{% equation %}n^{2}{% endequation %} ולהיוותר עם ה"משוואה" הבאה:</p>

<p>{% equation %}O\left(n\right)=O\left(n^{2}\right){% endequation %}</p>

<p>עכשיו, אנחנו נוהגים לחשוב על שוויון כיחס סימטרי. כלומר, אם {% equation %}O\left(n\right)=O\left(n^{2}\right){% endequation %} אז היינו מצפים שיתקיים גם {% equation %}O\left(n^{2}\right)=O\left(n\right){% endequation %}. רק שזה לא נכון, כי {% equation %}n^{2}{% endequation %} לא מקיימת {% equation %}n^{2}=O\left(n\right){% endequation %} (לא קשה להוכיח את זה). מכאן שהשימוש בסימן השוויון כאן הוא בעייתי. לי עצמי אין בעיה גדולה עם ויתור על הסימטריה של השוויון - אני חושב על {% equation %}a=b{% endequation %} בהקשר הזה כאומרת "{% equation %}a{% endequation %} הוא {% equation %}b{% endequation %}, אפילו אם לא בהכרח {% equation %}b{% endequation %} הוא {% equation %}a{% endequation %}" אבל לאנשים רבים זה כן מפריע. למי שזה מפריע לו אני יכול להגיד בעיקר - זה סימון. מטרתו לעשות את החיים קלים יותר. הוא מאוד מועיל כשרוצים לעשות שרשרת של שוויונות (מה שקורה כאשר מפשטים באופן הדרגתי ביטוי מסובך כלשהו). חבל לוותר עליו.</p>

<p>בגלל הבעייתיות הזו לפעמים מגדירים את {% equation %}O\left(g\left(n\right)\right){% endequation %} בתור מחלקת כל הפונקציות שמקיימות את התכונה שסימנתי כ-{% equation %}f\left(n\right)=O\left(g\left(n\right)\right){% endequation %} (במילים אחרות, {% equation %}f\left(n\right)\in O\left(g\left(n\right)\right){% endequation %} אם ורק אם קיימים {% equation %}c,n_{0}{% endequation %} כך ש-{% equation %}f\left(n\right)&lt;cg\left(n\right){% endequation %} לכל {% equation %}n>n_{0}{% endequation %}). עם זאת, בפועל אני לא מכיר מקומות שמשתמשים ב-{% equation %}\in{% endequation %} בהקשר הזה אלא תמיד בסימן השוויון המושמץ. התרגלתי.</p>

<p>נסכם: אפשר להשתמש ב-{% equation %}O{% endequation %} בחופשיות בתוך משוואות, אבל אם הוא מופיע בהן צריך לזכור שהמשוואה אינה סימטרית. למשל, במשוואה {% equation %}n+O\left(n^{2}\right)=n^{2}+O\left(n\right){% endequation %}, מה שצריך להבין הוא ש<strong>לכל</strong> פונקציה {% equation %}h\left(n\right)\in O\left(n^{2}\right){% endequation %}, <strong>קיימת</strong> פונקציה {% equation %}h^{\prime}\left(n\right)\in O\left(n\right){% endequation %} כך ש-{% equation %}n+h\left(n\right)=n^{2}+h^{\prime}\left(n\right){% endequation %}. כך זה באופן כללי, גם כשיש יותר מסימון אסימפטוטי אחד בכל אגף - לכל השמה של ערכים מתאימים לסימונים האסימפטוטיים באגף שמאל, קיימת השמה לסימונים באגף ימין כך שיתקיים שוויון.</p>

<p>בואו נעבור להיכרות עם שאר הסימנים האסימפטוטיים. עכשיו, משהבנו את הרעיון, יתר הסימנים יהיו ברורים כמעט מייד. נתחיל מאו-קטן: {% equation %}f\left(n\right)=o\left(g\left(n\right)\right){% endequation %} פירושו ש-{% equation %}f{% endequation %} קטנה <strong>ממש</strong> אסימפטוטית מ-{% equation %}g\left(n\right){% endequation %}. פורמלית, זה אומר ש<strong>לכל</strong> {% equation %}c>0{% endequation %} קיים {% equation %}n_{0}{% endequation %} כך ש-{% equation %}f\left(n\right)&lt;c\cdot g\left(n\right){% endequation %} לכל {% equation %}n>n_{0}{% endequation %}. בלשון גבולות, אם מתקיים {% equation %}\lim_{n\to\infty}\frac{f\left(n\right)}{g\left(n\right)}=0{% endequation %} אז {% equation %}f\left(n\right)=o\left(g\left(n\right)\right){% endequation %}.</p>

<p>סימונים דומים יש עבור חסמים תחתונים: {% equation %}f\left(n\right)=\Omega\left(g\left(n\right)\right){% endequation %} אם {% equation %}g\left(n\right)=O\left(f\left(n\right)\right){% endequation %}, ו-{% equation %}f\left(n\right)=\omega\left(g\left(n\right)\right){% endequation %} אם {% equation %}g\left(n\right)=o\left(f\left(n\right)\right){% endequation %}. הסימון האחרון, {% equation %}\Theta{% endequation %}, בא לציין חסם הדוק אסימפטוטית - חסם שהוא גם עליון וגם תחתון בו זמנית. {% equation %}f\left(n\right)=\Theta\left(g\left(n\right)\right){% endequation %} פירושו ש-{% equation %}f\left(n\right)=O\left(g\left(n\right)\right){% endequation %} וגם {% equation %}f\left(n\right)=\Omega\left(g\left(n\right)\right){% endequation %}, או באופן מפורש שקיימים קבועים {% equation %}c_{1},c_{2}{% endequation %} ו-{% equation %}n_{0}{% endequation %} כך ש-{% equation %}c_{1}\cdot g\left(n\right)\le f\left(n\right)\le c_{2}\cdot g\left(n\right){% endequation %} לכל {% equation %}n>n_{0}{% endequation %}.</p>

<p>סימון אחד שכדאי להתייחס אליו במפורש הוא הסימון {% equation %}f\left(n\right)=O\left(1\right){% endequation %}. כאשר {% equation %}1{% endequation %} בא לציין את הפונקציה הקבועה 1, ומה ש-{% equation %}f\left(n\right)=O\left(1\right){% endequation %} אומר הוא ש-{% equation %}f\left(n\right){% endequation %} חסומה על ידי קבוע (קיים {% equation %}c{% endequation %} כך ש-{% equation %}f\left(n\right)&lt;c{% endequation %} לכל {% equation %}n{% endequation %}). בדומה, {% equation %}f\left(n\right)=o\left(1\right){% endequation %} בא לציין פונקציה ששואפת לאפס כאשר {% equation %}n{% endequation %} שואף לאינסוף - עבור פונקציות מטבעיים לטבעיים זה לא ממש קורה, אבל בהקשרים אחרים זה בהחלט יכול לקרות. בואו נראה דוגמה פשוטה: הפונקציה {% equation %}f\left(x\right)=\frac{1}{x}{% endequation %} מקיימת {% equation %}f\left(x\right)=o\left(1\right){% endequation %} כאשר {% equation %}x{% endequation %} שואף לאינסוף. כמו כן, {% equation %}f\left(x\right)=x{% endequation %} מקיימת {% equation %}f\left(x\right)=o\left(1\right){% endequation %} כאשר {% equation %}x{% endequation %} שואף לאפס. כפי שאתם רואים, חשוב שיהיה ידוע ברקע לאן {% equation %}x{% endequation %} שואף.</p>

<p>עכשיו אפשר להבין את הסימון מתחילת הפוסט. משפט ידוע במתמטיקה, ש<a href="http://www.gadial.net/2008/01/20/lim_sin_x_over_x/">כבר הקדשתי לו פוסט בעבר</a>, הוא שמתקיים {% equation %}\lim_{x\to0}\frac{\sin x}{x}=1{% endequation %}. אפשר לנסח את זה בתור {% equation %}\sin x=O\left(x\right){% endequation %} עבור {% equation %}x{% endequation %} שואף לאפס. אפשר גם יותר טוב מזה - אנחנו יודעים שטור הטיילור של {% equation %}\sin x{% endequation %} מתחיל כך: {% equation %}\sin x=x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\dots{% endequation %}. אפשר לכתוב את זה גם כך: {% equation %}\sin x=x+o\left(1\right){% endequation %}, פשוט כי {% equation %}\left(-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\dots\right)=o\left(1\right){% endequation %} כאשר {% equation %}x{% endequation %} שואף לאפס. למעשה, אפשר גם לכתוב {% equation %}\sin x=x+O\left(x^{3}\right){% endequation %} וזה יהיה חסם אפילו יותר טוב (זכרו - כשאיקס שואף לאפס, חזקה גדולה יותר של איקס תיתן לנו משהו קטן יותר). זו דוגמה קטנה לאופן שבו הסימון הזה מופיע בחלקי מתמטיקה שאינם מדעי המחשב - כדאי לציין שהוא עתיק הרבה יותר ממדעי המחשב עצמם.</p>

<p>ועכשיו לבחון את עצמכם! האם, אחרי קריאת הפוסט, אתם מבינים מה לכל הרוחות ניסיתי לומר בכותרת שלו? אם כן, סימן שהצלחתי! </p>

