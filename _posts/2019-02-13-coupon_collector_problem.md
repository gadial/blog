---
id: 3747
title: "בעיית איסוף הקופונים"
date: 2019-02-13 14:34:18
layout: post
categories: 
  - הסתברות
tags: 
  - בעיית איסוף הקופונים
  - הסתברות
  - מספרים הרמוניים
  - קבוע אוילר מסקרוני
---
הנה לכם סיפור על איך בעיות מתמטיות צצות מעצמן. זה לא מכבר יצא לאוויר העולם משחק הוידאו Super Smash Bros. Ultimate שהוא נצר לשושלת ארוכה ומפוארת של משחקי מכות שמאחדים דמויות משלל משחקים בלתי קשורים בעליל על מנת שירביצו אחד לשני באווירה של כאוס מוחלט בשלל זירות שונות ומשונות שנלקחות גם כן משלל משחקים בלתי קשורים בעליל. המשחק הנוכחי החליט לקחת את המופרכות הזו לשיאים חדשים על ידי כך שיאגד את כל הדמויות והזירות מכל המשחקים שיצאו עד כה בסדרה, ויוסיף עוד. כתוצאה מכך יש לא פחות מ-103 זירות במשחק. מסך בחירת הזירות נראה כך:

<img class="alignnone size-full wp-image-3748" src="{{site.baseurl}}{{site.post_images}}/2019/02/gw44pdhlx3i11.png" alt="" width="1600" height="900" />

עם כל כך הרבה זירות, למי יש זמן לבחור בכלל? אני תמיד בוחר בסימן השאלה למעלה שבוחר אחת מ-103 הזירות באקראי, כך שיש הסתברות שווה לכל אחת מהזירות. והנה שמתי לב שגם עכשיו, אחרי חודשיים של משחק, עדיין קורה שאני משחק בזירה שאני לא זוכר שראיתי קודם. זה העלה אצלי את השאלה הבאה: תוך כמה סיבובים של המשחק אפשר לראות את כל הזירות?

ובכן, זו שאלה מוכרת בתורת ההסתברות שנקראת "בעיית איסוף הקופונים" (שם שלא הכרתי עד עכשיו). הרעיון אצל איסוף הקופונים דומה: נניח שחברת דגני בוקר יוצאת במבצע שבו בכל אריזה שלה יש קופון שנבחר באקראי מבין כמה אפשריים, ומי שאוסף את כל הקופונים זוכה בפרס - כמה אריזות דגנים צריך לקנות? כמובן, בניסוח הזה של הבעיה צריך לחדד את העובדה שלכל קופון יש הסתברות שווה להופיע; אם זה לא המצב, אז הניתוח המתמטי מסובך בהרבה, מעבר למה שאני רוצה לכסות בפוסט הזה.

בואו נתמודד עם בעיית הזירות האקראיות שלי; בשלב הראשון האתגר יהיה בכלל לנסח את השאלה בצורה נכונה. מה שברור מייד הוא שצריך <strong>לפחות</strong> 103 סיבובים של המשחק כדי לראות את כל הזירות. אם הייתי עובר על הזירות באופן שיטתי, זה גם כל מה שהייתי צריך; אבל אני מפקיד את השליטה בידי הגורל העיוור שמגריל לי זירה בכל פעם, ולכן בהחלט ייתכן שלא משנה כמה משחקים אשחק, <strong>תהיה זירה שלא אראה אף פעם</strong>. היא פשוט אף פעם לא תעלה בגורל. ההסתברות לכך היא אפסית ובהמשך נראה שהיא לא באמת משפיעה על החישוב, אבל לא חייבים ללכת לקיצוניות: נניח שב-102 הסיבובים הראשונים באמת ראיתי זירה חדשה בכל פעם, ואז במשחק ה-103 פתאום הוגרלה זירה שכבר ראיתי. זה כבר אומר שבמקרה הזה, אזדקק לפחות ל-104 סיבובים. אז מספר <strong>מדויק</strong> לא הולך לענות לשאלה שלי, כי מספר הסיבובים תלוי במזל שלנו. השאלה המדויקת יותר היא מה יהיה <strong>מספר הסיבובים הממוצע</strong>.

למה אני מתכוון בממוצע? נניח שניתן ל-10,000 שחקנים לשחק במשחק ולספר לנו כמה סיבובים חלפו עד שהם ראו את כל הזירות, ואז ניקח את הממוצע החשבוני של התוצאות הללו - כלומר, נחבר את כולן ונחלק במספר השחקנים, שהוא 10,000: מה המספר שנקבל אז? על פי רוב נקבל מספרים שהם כמעט זהים; <strong>חוק המספרים הגדולים</strong> בהסתברות מבטיח לנו את זה.

כמובן, אין טעם באמת לתת לשחקנים לשחק; אפשר לעשות משהו מהיר יותר - סימולציה במחשב. אז הנה קוד בשפת פייתון שעושה בדיוק את זה:

<div class="code-block">
{% highlight python %}
import random

def experiment(n):
    visited = [False] * n
    visited_count = 0
    rounds = 0
    while visited_count &lt; n:
        rounds += 1
        i = random.randrange(n)
        if not visited[i]:
            visited[i] = True
            visited_count += 1           
    return rounds

tries = 10000
N = 103
total = 0
for i in range(tries):
    total += experiment(N)
print(total / tries)
{% endhighlight %}
</div>

כשהרצתי את הקוד לקח לו רגע לסיים ובסוף קיבלתי את התוצאה {% equation %}535.3524{% endequation %}. בהרצה נוספת קיבלתי {% equation %}540.0647{% endequation %}. זה כבר מעורר את החשד ש-10,000 זה לא מספיק ואולי עדיף 100,000 הרצות בשביל תוצאה מדויקת יותר. אז הרצתי גם 100,000 פעמים, זה לקח יותר זמן וקיבלתי {% equation %}537.58746{% endequation %}. האם אפשר יותר מדויק, יותר מהר? ובכן, כן! אם נכניס לתמונה את תורת ההסתברות. כמו כן, כדי לפשט לעצמנו קצת את החיים נפסיק לדבר על המספר 103 דווקא ונדבר על מספר {% equation %}N{% endequation %} כללי.

יש לי <a href="https://gadial.net/2010/07/29/probability_intro/">פוסטים מפורטים יותר</a> בבלוג על תורת ההסתברות כך שלא אחזור על כל הפרטים כעת, אבל הנה הרעיון. כשאנחנו באים למדל משהו באמצעות תורת ההסתברות אנחנו קודם כל מגדירים <strong>מרחב מדגם</strong> שכולל את כל התוצאות האפשריות של ההגרלה שאנחנו מבצעים. במקרה הנוכחי אפשר לחשוב על הסיטואציה כאילו אנחנו מגרילים סדרה של זירות (שיכולה להיות סופית או אינסופית), כך שכל סדרה מסתיימת אחרי שכל זירה הופיעה לפחות פעם אחת. סדרה אינסופית מצביעה על כישלון - שיש זירה אחת לפחות שלא נראתה אף פעם. אפשר להראות שההסתברות של סדרה אינסופית שכזו היא אפס; זה לא אומר שאין סיכוי שהיא תופיע, רק שהסיכוי הזה <strong>זניח</strong> (הסבר מלא יותר יצטרך להיכנס לעובי הקורה הטכני של מרחבי הסתברות רציפים).

עכשיו אפשר להגדיר על מרחב ההסתברות שלנו <strong>משתנה מקרי</strong>. משתנה מקרי זו פונקציה שלוקחת תוצאה ממרחב המדגם ומחזירה ערך מספרי כלשהו שהיא מסמלת - במקרה הזה, אפשר להתאים לכל סדרה פשוט את האורך שלה. נסמן את המשתנה המקרי הזה ב-{% equation %}X{% endequation %}. עכשיו אפשר לשאול שאלה כמו "מה ההסתברות שאם נגריל סדרה כלשהי, הערך של {% equation %}X{% endequation %} יהיה לפחות 17?". ואפשר גם לשאול מה יהיה הערך <strong>הממוצע</strong> של {% equation %}X{% endequation %}. בתורת ההסתברות קוראים לערך ממוצע כזה <strong>התוחלת</strong> של {% equation %}X{% endequation %}, מסמנים אותו ב-{% equation %}E\left[X\right]{% endequation %} והוא מוגדר ככה: {% equation %}E\left[X\right]=\sum_{a}a\cdot\text{P}\left(X=a\right){% endequation %}, כלומר - זה סכום משוקלל של כל הערכים {% equation %}a{% endequation %} שהמשתנה המקרי עשוי להחזיר, כשהמשקל של כל {% equation %}a{% endequation %} כזה הוא ההסתברות ש-{% equation %}X{% endequation %} יחזיר אותו.

מה שאני רוצה לעשות מכאן והלאה הוא לחשב את {% equation %}E\left[X\right]{% endequation %} עבור בעיית הקופונים שלנו. לצורך כך אני אעזר בתכונה מועילה במיוחד: <strong>לינאריות התוחלת</strong>. מה שלינאריות התוחלת אומרת הוא פשוט מאוד: {% equation %}E\left[X+Y\right]=E\left[X\right]+E\left[Y\right]{% endequation %}. כלומר: אם יש לנו שני משתנים מקריים, {% equation %}X,Y{% endequation %}, ואנחנו בונים משתנה מקרי חדש שהוא סכום של שניהם (כלומר: לכל איבר במרחב המדגם הוא מפעיל את {% equation %}X,Y{% endequation %} על האיבר הזה, מקבל תוצאות ומחבר אותן) אז התוחלת של המשתנה החדש תהיה הסכום של התוחלות של המשתנים. ההוכחה של לינאריות התוחלת לא קשה, אבל לא אציג אותה כאן.

איך זה עוזר לנו? ראשית, אם זה עובד לשני משתנים, זה עובד לכל מספר סופי של משתנים: אם {% equation %}X=X_{1}+X_{2}+\dots+X_{N}{% endequation %} אז {% equation %}E\left[X\right]=E\left[X_{1}\right]+E\left[X_{2}\right]+\dots+E\left[X_{N}\right]{% endequation %}. שנית, אני טוען שאת ה-{% equation %}X{% endequation %} שלנו של בעיית הקופונים אכן אפשר להציג בתור סכום שכזה. הרעיון? המשתנה {% equation %}X_{i}{% endequation %} סופר את מספר הסיבובים שנדרשו כדי להעלות את מספר הזירות שראינו עד כה מ-{% equation %}i-1{% endequation %} אל {% equation %}i{% endequation %}.

בצורה הזו ברור ש-{% equation %}X{% endequation %} הוא אכן הסכום המבוקש: {% equation %}X{% endequation %} הוא מספר הסיבובים הכולל שנדרש כדי להעלות את מספר הזירות שראינו מ-0 אל {% equation %}N{% endequation %}; זה שווה לזמן שנדרש כדי לעלות מ-0 אל 1, ועוד הזמן שנדרש לעלות מ-1 אל 2 וכן הלאה עד אשר הגענו מ-{% equation %}N-1{% endequation %} אל {% equation %}N{% endequation %}.

כל מה שנותר לעשות הוא לחשב את {% equation %}E\left[X_{i}\right]{% endequation %} - תוחלת הזמן שנדרשת כדי להעלות את מספר הזירות שראינו כבר מ-{% equation %}i-1{% endequation %} אל {% equation %}i{% endequation %}. אלא שאת זה קל לעשות כי {% equation %}X_{i}{% endequation %} הוא <strong>משתנה גאומטרי</strong>, וזה מושג מוכר ואהוב מתורת ההסתברות. משתנה גאומטרי מתעסק בשאלה "אם מטילים שוב ושוב את אותה הקוביה, כמה זמן יעבור עד שנקבל 1"? באופן כללי יותר, משתנה גאומטרי מדבר על הסיטואציה שבה יש ניסוי עם הסתברות {% equation %}p{% endequation %} להצליח, ואנחנו חוזרים עליו שוב ושוב עד אשר הוא מצליח וסופרים כמה נסיונות נדרשו לנו.

את התוחלת של הדבר הזה אפשר לחשב בעזרת הנוסחה {% equation %}E\left[X\right]=\sum_{a}a\cdot\text{P}\left(X=a\right){% endequation %} והיכרות כלשהי עם סכומים אינסופיים. ההוכחה תהיה קצת טכנית ואפשר לדלג עליה מבלי לפגוע בהמשך הפוסט.

{% equation %}\text{P}\left(X=1\right){% endequation %} הוא {% equation %}p{% endequation %} (ההסתברות שנצליח בניסוי הראשון).

{% equation %}\text{P}\left(X=2\right){% endequation %} הוא {% equation %}\left(1-p\right)p{% endequation %} (ההסתברות <strong>שניכשל</strong> בניסוי הראשון - זה ה-{% equation %}\left(1-p\right){% endequation %} - כפול ההסתברות שנצליח בניסוי השני).

{% equation %}\text{P}\left(X=3\right){% endequation %} הוא {% equation %}\left(1-p\right)^{2}p{% endequation %} ומכאן כבר אפשר לראות את הכיוון הכללי:

{% equation %}E\left[X\right]=\sum_{n=1}^{\infty}n\text{P}\left[X=n\right]=\sum_{n=1}^{\infty}n\cdot p\cdot\left(1-p\right)^{n-1}=p\sum_{n=1}^{\infty}n\left(1-p\right)^{n-1}{% endequation %}

וכעת מגיע להטוט לא טריוויאלי. בואו נכתוב שוב את הטור שיש לנו, אבל עם סימונים קצת שונים:

{% equation %}\sum_{n=1}^{\infty}nx^{n-1}{% endequation %}

אלו מכם שמכירים חדו"א אולי מזהים שהאיבר שנמצא בתוך הטור נראה כמו <strong>נגזרת</strong> לפי {% equation %}x{% endequation %} של פונקציה. כלומר, אפשר לכתוב

{% equation %}\sum_{n=1}^{\infty}nx^{n-1}=\sum_{n=1}^{\infty}\left(x^{n}\right)^{\prime}=\left(\sum_{n=1}^{\infty}x^{n}\right)^{\prime}{% endequation %}

המעבר האחרון, שבו "הוצאתי את הנגזרת החוצה מהסכום" הוא לא טריוויאלי ודורש הצדקות בחדו"א - אבל במקרה הזה, זה עובד. עכשיו מה שקיבלנו בתוך הסכום הוא <strong>טור גאומטרי</strong> בסיסי שאנחנו יודעים את הנוסחה שלו:

{% equation %}\sum_{n=1}^{\infty}x^{n}=\frac{x}{1-x}{% endequation %}

הנוסחה הזו עובדת רק עבור {% equation %}\left|x\right|&lt;1{% endequation %}, אבל מכיוון שנציב {% equation %}x=1-p{% endequation %} ואנחנו מניחים ש-{% equation %}p&gt;0{% endequation %} זו לא בעיה.

לבסוף, צריך עדיין <strong>לגזור</strong> את {% equation %}\frac{x}{1-x}{% endequation %}. הנגזרת יוצאת {% equation %}\frac{\left(1-x\right)+x}{\left(1-x\right)^{2}}=\frac{1}{\left(1-x\right)^{2}}{% endequation %}, וכשנציב {% equation %}x=1-p{% endequation %} חזרה נקבל

{% equation %}p\sum_{n=1}^{\infty}n\left(1-p\right)^{n-1}=\frac{p}{\left(1-\left(1-p\right)\right)^{2}}=\frac{p}{p^{2}}=\frac{1}{p}{% endequation %}

וכעת אפשר לחזור אל בעיית הקופונים שלנו. ראינו כבר ש-{% equation %}E\left[X\right]=E\left[X_{1}\right]+E\left[X_{2}\right]+\dots+E\left[X_{N}\right]{% endequation %}. נשאר רק להבין - לכל {% equation %}X_{i}{% endequation %}, מהו {% equation %}p{% endequation %} שלו? מה ההסתברות להצליח?

הניסוי של {% equation %}X_{i}{% endequation %} מצליח אם אנחנו מעלים בגורל זירה חדשה שטרם עלתה בגורל. עד כה עלו בגורל {% equation %}i-1{% endequation %} זירות, מה שאומר שנותרו עוד {% equation %}N-\left(i-1\right){% endequation %} זירות. מספר הזירות הכולל הוא {% equation %}N{% endequation %}, ולכן ההסתברות להעלות בגורל את אחת מהזירות החדשות היא {% equation %}\frac{N-\left(i-1\right)}{N}{% endequation %}. כלומר:

{% equation %}E\left[X_{i}\right]=\frac{1}{p_{i}}=\frac{N}{N-\left(i-1\right)}{% endequation %}

כלומר:

{% equation %}E\left[X_{1}\right]=\frac{N}{N}=1{% endequation %}

{% equation %}E\left[X_{2}\right]=\frac{N}{N-1}{% endequation %}

וכן הלאה עד {% equation %}E\left[X_{N}\right]=\frac{N}{N-\left(N-1\right)}=\frac{N}{1}{% endequation %}.

וקיבלנו:

{% equation %}E\left[X\right]=\sum_{i=0}^{N-1}\frac{N}{N-i}=N\sum_{i=0}^{N-1}\frac{1}{N-i}=N\sum_{i=1}^{N}\frac{1}{i}{% endequation %}

וכאן אנחנו פוגשים חברים ותיקים (של חלקנו...). הסכום {% equation %}\sum_{i=1}^{N}\frac{1}{i}{% endequation %} (ובסימון אחר: {% equation %}1+\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{N}{% endequation %}) הוא כל כך חשוב שהוא זוכה לאות מיוחדת משלו: {% equation %}H_{N}=\sum_{i=1}^{N}\frac{1}{i}{% endequation %}, והמספר הזה נקרא <strong>המספר ההרמוני</strong> ה-{% equation %}N{% endequation %}-י. אלו מספרים מוכרים ואהובים שצצים במתמטיקה בשלל הזדמנויות, כך שלומר שפתרון בעיית הקופונים הוא שתוחלת הזמן עבור {% equation %}N{% endequation %} קופונים היא {% equation %}N\cdot H_{N}{% endequation %} היא פתרון קביל בהחלט.

אבל בואו ננסה לשכנע אתכם עוד קצת שזה אחלה פתרון.

כזכור, התחלתי את הדיון עם סוגייה קונקרטית - כמה סיבובים של Super Smash Bros. Ultimate צריך בתוחלת כדי לראות את כל הזירות? ועוד לפני שהכנסתי את תורת ההסתברות לתמונה ניסיתי לתת תשובה "אמפירית" לשאלה הזו על ידי קוד שמבצע סימולציות ומחשב ממוצעים. הקוד הזה <strong>עובד</strong>, אבל יש לו שני חסרונות ברורים:
<ol>
 	<li>לוקח לו הרבה זמן לרוץ, יחסית.</li>
 	<li>התוצאה שהוא מחזיר היא <strong>קירוב</strong> של התוחלת, לא הערך המדויק שלה.</li>
</ol>
הנוסחה שמצאתי עכשיו, {% equation %}N\cdot H_{N}{% endequation %}, לא נותנת קירוב של התוחלת אלא את התוחלת עצמה, במדויק; אבל עוד יותר חשוב מכך, אפשר לחשב אותה <strong>מהר</strong>, בשורה אחת של פייתון:

<div class="code-block">
{% highlight python %}
print(N * sum(1 / k for k in range(1,N+1)))
{% endhighlight %}
</div>

השורה הזו מחזירה את המספר {% equation %}537.3294902186476{% endequation %} שהוא התוחלת ה"נכונה"; אפשר לראות שתוצאת הניסוי שעשיתי קודם יצאה קרובה מאוד (537 ומשהו) אבל בשביל זה הייתי צריך להקפיץ את מספר החזרות על הניסוי מ-10,000 (שלא נתן משהו עד כדי כך מדויק) אל 100,000 וזה לקח הרבה יותר זמן. הפתרון המדויק שמצאתי הוא <strong>יעיל יותר לחישוב</strong> ולכן טוב יותר. אני מדגיש את הנקודה הזו כי הפתרון הזה הוא לא "נוסחה סגורה" - יש בו סכום שתלוי ב-{% equation %}N{% endequation %}, ועשויה להיות רתיעה מסכומים כאלו למי שרגילים לתרגילים מקומבינטוריקה בסיסית שבהם לתת נוסחה שכזו לפעמים גורם להורדת נקודות כי זה לא פתרון פשוט "מספיק". ובכן, אם אתם סובלים (כמו שאני סבלתי) מטראומה כזו מסכומים - אל! סכומים יכולים להיות מאוד מועילים לפעמים (ודוגמא טובה מאוד היא <strong>עקרון ההכלה וההפרדה</strong> <a href="https://gadial.net/2011/12/31/inclusion_exclusion_principle/">שכתבתי עליו כבר פוסט</a>, ומאפשר להמיר בעיות חישוביות קשות למדי במשימות חישוביות הרבה יותר קלות למרות שהוא מתבסס על סכום).

אבל יש לנוסחה שהגענו אליה עוד יתרון - קיים לה <strong>קירוב</strong> טוב מאוד, שנובע מכמה טוב אנחנו מבינים מספרים הרמוניים. אפשר להראות (אין לי מושג איך - צריך יהיה לכתוב על זה פעם פוסט!) שמספרים הרמוניים מתנהגים "בערך" כמו הלוגריתם הטבעי. קצת יותר בפירוט:

{% equation %}H_{N}\approx\ln N+\gamma+\frac{1}{2N}{% endequation %}

כאשר {% equation %}\gamma=0.5772156649\dots{% endequation %} נקרא <strong>קבוע אוילר-מסקרוני</strong> והוא מספר מעניין בפני עצמו (למשל: עד היום אנחנו לא יודעים אם הוא רציונלי או לא).

אם נכפיל את הנוסחה הזו ב-{% equation %}N{% endequation %}, נקבל את הקירוב הבא לבעיית הקופונים:

{% equation %}N\ln N+\gamma N+\frac{1}{2}{% endequation %}

וזו נוסחה ש<strong>מאוד קל</strong> לחשב ביעילות, גם אם הערך של {% equation %}N{% endequation %} הוא אדיר (בן מאות ספרות - מה שמונע לגמרי חישוב של הסכום {% equation %}1+\frac{1}{2}+\dots+\frac{1}{N}{% endequation %}). ככל ש-{% equation %}N{% endequation %} גדול יותר כך הקירוב יהיה טוב יותר; עד כמה הוא טוב עבור {% equation %}N=103{% endequation %}? ובכן, הבה וננסה:

<div class="code-block">
{% highlight python %}
import numpy
gamma = 0.5772156649
print(N * numpy.log(N) + gamma * N + 1/2)
{% endhighlight %}
</div>

הקוד הזה, עבור {% equation %}N=103{% endequation %}, מניב את התוצאה {% equation %}537.3302992723525{% endequation %} שהיא קרובה להפליא אל התוצאה המדויקת, והחישוב שלה כמובן מהיר יותר. אם אני אנסה להריץ את החישובים הקודמים עבור {% equation %}N=1000000000000000{% endequation %} אני אכשל בצורה מזעזעת (הקוד ירוץ וירוץ ולעולם לא יסיים) אבל עם הקירוב הזה אני עדיין אקבל תוצאה תוך חלקיק שניה - ואני יודע שזו תהיה תוצאה שלא אוכל להבדיל בינה ובין התוצאה ה"אמיתית".

זה סוגר את בעיית הקופונים הבסיסית, אבל כמובן שמכאן והלאה המתמטיקאים משתוללים עם שלל וריאציות: מה אם לא כל קופון הוא בעל אותה הסתברות להיבחר? מה אם אנחנו לא קונים קופונים אלא מנסים להשלים את כל המדבקות באלבום של "חבורת הזבל" (כן! היה משהו כזה!) ובכל חבילת מדבקות שאנחנו קונים יש שש מדבקות ולא רק אחת? וכן הלאה וכן הלאה. אבל אני לא אתעסק בזה עכשיו ומקווה שתסלחו לי; יש לי 537 סיבובים של Super Smash Bros. Ultimate לשחק בהם.