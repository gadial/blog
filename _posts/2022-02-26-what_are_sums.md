---
title: "מה זה בכלל סכום?"
layout: post
categories:
  - כללי
tags:
  - סכום
description: 'מה זה בעצם סכום? איך מסמנים אותו? למה הוא יכול להיות אינסופי?'
image: "2022/dichotomy-paradox.png"
social_media_share: true

---

אני רוצה לדבר על אחד המושגים הפשוטים במתמטיקה - <strong>חיבור</strong>. להתחיל מהפשוט והמוכר ולהגיע אל המחוזות הקצת פחות פשוטים ומוכרים. ספציפית, הייתי רוצה שעד סוף הפוסט כולנו נרגיש בנוח עם המפלצת הבאה:


{% equation %} \sum_{n=1}^{\infty}\frac{1}{2^{n}} = 1 {% endequation %}


האם זה נראה כרגע כמו אוסף אקראי של סימונים? מצוין, אני מקווה שזה הולך להיות הפוסט בשבילכם.

נתחיל מההתחלה - מה זה חיבור? כאן יש אינטואיציה אפילו לילדים. אם יש לנו שני תפוחים בשקית אחת ושלושה תפוחים בשקית שניה, ואנחנו שופכים את תוכן שתי השקיות לקערה, אז בקערה יהיו {% equation %}2+3=5{% endequation %} תפוחים. נקודת המוצא שלי בפוסט הזה היא שהאינטואיציה הזו יושבת לנו טוב. כמובן, יש מרחק כלשהו בין האינטואיציה ובין היכולת הטכנית לבצע את הפעולה. איך נחשב, למשל, את החיבור התמים {% equation %}52321+437681{% endequation %}? התשובה הנכונה היא "עם מחשבון" כי אין שום סיבה לעשות כזה דבר ידנית, אבל יש קסם בשם <strong>חיבור ארוך</strong> שמאפשר לנו לעשות את זה ידנית בקלות יחסית. <a href="https://gadial.net/2020/11/18/how_to_addition/">יש לי פוסט עליו</a> ואני לא הולך להציג אותו שוב כאן.

אנחנו בסדר עם חיבור של שני מספרים? נפלא, בואו נסבך מאוד את הסיטואציה ונעבור לדבר על חיבור של <strong>שלושה</strong> מספרים. למשל {% equation %}2+3+5=10{% endequation %}. זה לא נראה מסובך יותר, וגם האינטואיציה פשוטה - יש לנו שלוש שקיות של תפוחים, אנחנו שופכים את כולן לקערה ורואים מה יוצא. זו אינטואיציה מצוינת כי אנחנו רואים כמה אפשר לבצע את הפעולה "לשפוך את השקיות לקערה" בלי לחשוב עד הסוף על מה שעושים - מה <strong>הסדר</strong> שבו אנחנו מרוקנים את השקיות. זה נשמע לנו אווילי בכלל להתייחס לזה, כי איך זה ישפיע על התוצאה? וזה אכן לא משפיע. מבחינה מתמטית אין הבדל בין {% equation %}2+3{% endequation %} ובין {% equation %}3+2{% endequation %}, וקוראים לזה <strong>חוק החילוף</strong>, וגם אין הבדל בין קודם לרוקן את השקיות של {% equation %}2,3{% endequation %} ואחר כך לרוקן את השקית של {% equation %}5{% endequation %} לקערה החצי מלאה, ובין קודם לרוקן את השקיות של {% equation %}3,5{% endequation %} ביחד ורק אז לרוקן את זו של 2, מה שאנחנו מסמנים בתור {% equation %}\left(2+3\right)+5=2+\left(3+5\right){% endequation %} וקוראים לו <strong>חוק הקיבוץ</strong>.

חוק החילוף די מובן מאליו, אבל על חוק הקיבוץ כדאי לתת הסבר נוסף. ראשית, הנה סיטואציה שבה הוא לא עובד: חיסור. {% equation %}5-\left(3-1\right)=3{% endequation %} אבל {% equation %}\left(5-3\right)-1=1{% endequation %}. כלומר, כשאני מסתכל על ביטוי כמו {% equation %}5-3-1{% endequation %} ומחשב אותו ומקבל 1, אני בעצם באופן מובלע אומר שקודם כל אחשב את החיסור השמאלי יותר ואז את הימני יותר. אנחנו אולי רגילים לזה כי כך עשינו מילדות, אבל זו בסופו של דבר <strong>מוסכמה שרירותית</strong> שחלקנו לא מודעים אליה. העובדה שחיבור מקיים את חוק הקיבוץ משמעותה שבכל הנוגע לחיבור, המוסכמה הזו לא משנה - גם המוסכמה ההפוכה הייתה מניבה את אותה תוצאה.

אבל חוק הקיבוץ ממחיש לנו עוד נקודה שתהיה אפילו עוד יותר קריטית להמשך - אנחנו מתייחסים אל חיבור תמיד בתור פעולה שפועלת על <strong>שני איברים</strong>. לא יותר. הסימן {% equation %}+{% endequation %} תמיד מופיע כשיש משהו בצד ימין שלו ומשהו בצד שמאל שלו, והמשמעות היא "לחבר את מה שבצד ימין עם מה שבצד שמאל". אנחנו לא משתמשים בסימן + כדי להגיד "נא לחבר את שלושת האיברים הבאים", וזה דווקא עומד <strong>בניגוד לאינטואיציה</strong> שלנו. אם יש לי שלוש שקיות תפוזים, אני בהחלט יכול לקחת את שלושתן ולרוקן אותן לקערה <strong>בו זמנית</strong>. לא כך המצב במתמטיקה; אם תרצו, אני מסתכל על הביטוי {% equation %}2+3+5{% endequation %} בתור "תהליך" או "אלגוריתם" או איך שלא נרצה לקרוא לזה. הביטוי הזה בעצם אומר

<ul> <li>חברו את {% equation %}2{% endequation %} עם 3.</li>


<li>חברו את תוצאת השלב הקודם עם 5.</li>


<li>התוצאה הסופית היא תוצאת השלב הקודם.</li>

</ul>

חוק הקיבוץ מאפשר לנו לומר "בעצם, זה לא משנה מה יהיה סדר השלבים של החיבורים שלנו, אז למה לא לחשוב על {% equation %}2+3+5{% endequation %} בתור פעולת חיבור אחת שכולה מתבצעת בבת אחת?" וזה טוב ויפה ועובד מעולה. עד שמכניסים לתמונה את מושג ה<strong>אינסוף</strong> והכל מסתבך נורא. לכן אני מתעקש על נקודת המבט של ה"תהליך" כבר עכשיו.

בואו נדבר עכשיו על טריק מתמטי יפה ואהוב <a href="https://gadial.net/2019/05/30/arithmetic_and_geometric_series/">שכבר יש לי פוסט עליו</a> אבל תמיד טוב להזכיר אותו שוב. נניח שמבקשים ממני לחשב את הסכום

{% equation %}1+2+3+4+5+6+7+8+9+10{% endequation %}

מה אני יכול לעשות? ובכן, אני יכול להתחיל לחשב את הסכומים על ידי ביצוע תשע פעולות חיבור. זה נורא. אין מצב שאעשה את זה. אז כמובן, אני יכול לשלוף מחשבון. אבל זה <strong>עדיין</strong> נורא! עדיין צריך לכתוב את כל המספרים הללו! (אמנם, כתבתי אותם לפני שניה כי אני כותב את הפוסט אבל בואו נחליק את הנקודה הזו). אם יש עיקרון אחד שמנחה את המתמטיקה, זה העיקרון <strong>מתמטיקאים הם עצלנים</strong>. הם מחפשים את הדרך הקלה ביותר לבצע משהו, בטח אם זה משהו טכני מעיק. האגדה מספרת שהמתמטיקאי קארל פרידריך גאוס קיבל מהמורה שלו בבית הספר היסודי את המשימה של לחשב את הסכום הזה, רק לא עד 10 אלא עד 100, ומכיוון שהיה מתמטיקאי עצלן, במקום שיבצע את כל פעולות החיבור עלה על הטריק שאציג עכשיו ופתר את התרגיל בן רגע.

מה הטריק? אם נסתכל לשניה על האיבר הראשון והאחרון בסכום הזה ונחבר אותם, נקבל

{% equation %}1+10=11{% endequation %}

ואם נסתכל על האיבר השני והאיבר הלפני אחרון ונחבר אותם, נקבל

{% equation %}2+9=11{% endequation %}

וכך גם בהמשך:

{% equation %}3+8=11{% endequation %}

וכן הלאה. הרעיון די ברור - אפשר לחלק את <strong>כל</strong> המספרים בסכום לזוגות-זוגות, כך שסכום כל זוג הוא 11. יש בסך הכל 10 מספרים ולכן 5 זוגות, אז הסכום הכולל הוא {% equation %}5\times11=55{% endequation %}.

זה עובד תמיד; למשל, עם הסכום של גאוס שהמשיך עד 100 יש לנו 50 זוגות וסכום כל זוג הוא 101 ולכן התוצאה הכוללת היא {% equation %}50\times101=5050{% endequation %}. אפילו אם יש לנו מספר <strong>אי זוגי</strong> של מחוברים זה עדיין עובד; למשל, בסכום

{% equation %}1+2+3+4+5+6+7+8+9{% endequation %}

סכום כל זוג הוא 10, וכמה זוגות יש לנו? ובכן, המספר 5 הוא נטול בן זוג, אבל מי אמר שחייבים בן זוג? אפשר לחשוב על 5 לבדו כאילו הוא <strong>חצי זוג</strong>, ולכן הוא תורם למניין הזוגות הכולל {% equation %}\frac{1}{2}{% endequation %}. נקבל את המכפלה {% equation %}10\times4.5=45{% endequation %}, וזו כמובן התוצאה הנכונה.

אז זה היה טריק נחמד, אבל בשביל מה? בשביל לתת לי מוטיבציה לדבר על שיטת ה<strong>סימון</strong> שלנו לסכומים. הדרך הישירה ביותר לכתוב את התוצאה שראינו היא

{% equation %}1+2+3+4+5+6+7+8+9+10=55{% endequation %}

אבל זה פשוט לא לעניין - לכתוב סכום כל כך ארוך זה גם מתיש וגם לא נעים לקריאה. אז למתמטיקאים יש כמה שיטות לפשט את העניינים. ראשית, אם יש איזה שהוא עיקרון ברור מאחורי הסכום, אפשר להחביא את עיקר הפרטים מאחורי כתיב של שלוש נקודות. במקרה שלנו נכתוב

{% equation %}1+2+\ldots+10=55{% endequation %}

מה הולך כאן? כשקוראים את הביטוי הזה, מה שעושים בראש הוא להגיד "אה, האיבר הראשון הוא 1 והשני הוא 2? אז בטח השלישי הוא 3 וכן הלאה עד 10, כשכל פעם מגדילים ב-1". זה הגיוני ומתבקש, אבל זה <strong>לא מוגדר היטב</strong>. אם יבוא מישהו ויגיד "אה, האיבר הראשון הוא 1 והשני הוא 2? אז בטח השלישי הוא 4 והרביעי הוא 42 והחמישי הוא 1,545,154" וימשיך כך כיד הדמיון הטובה עליו, מה אנחנו אמורים לעשות? לומר לו "לא, אתה טועה?" אין כאן טועים וצודקים, זו קונבנציית סימון שבאמת לא מספרת את כל הסיפור. זה לא אומר שלא משתמשים בה; בהרבה ספרי מתמטיקה מניחים שהקוראים רוצים להיכנס לראש של הכותב (ולפעמים לא כל כך מסובך לעשות את זה!) ולא הולכים להתחכם אלא ללכת על הפרשנות הסבירה.

עדיין, אם רוצים שיטת סימון שהיא כן חד משמעית ומספרת את כל הסיפור, אפשר להשתמש בסימון המקוצר שהראיתי בתחילת הפוסט. בסימון הזה מופיעה האות היוונית סיגמא, {% equation %}\Sigma{% endequation %}, בגדול; האות הזו באה לומר "סכום". ליד האות הזו מגיע תיאור קומפקטי של האיברים שאנחנו סוכמים, וזאת באמצעות <strong>נוסחה</strong>, כלומר ביטוי כלשהו שיש בו משתנה שבו אנחנו מציבים ערכים ומקבלים כתוצאה מכך את הערכים שאנחנו סוכמים. בואו נתחיל את הדוגמאות שלנו עם משהו קצת יותר מתוחכם מהסכום שכבר ראינו - הסכום

{% equation %}1+4+9+16+25+\ldots+100{% endequation %}

שבו אנחנו סוכמים את <strong>הריבועים</strong> של המספרים הטבעיים מ-1 עד 10, כלומר זה בעצם הסכום

{% equation %}1^{2}+2^{2}+3^{2}+\ldots+10^{2}{% endequation %}

בנוסחה המקוצרת אנחנו נכתוב כך:

{% equation %}\sum_{n=1}^{10}n^{2}{% endequation %}

מה הולך פה? ה-{% equation %}n^{2}{% endequation %} שנמצא מימין ל-{% equation %}\Sigma{% endequation %} הוא הנוסחה עצמה: הוא מתאר את פעולת ההעלאה בריבוע. אני קורא בשם <strong>האיבר הכללי</strong> ל-{% equation %}n^{2}{% endequation %} הזה כי הוא מתאר בצורה כללית איך נראה איבר כלשהו בסכום (בצורה כללית, כלומר איך <strong>כלל</strong> האיברים בסכום נראים). ה-{% equation %}n=1{% endequation %} שנמצא למטה וה-{% equation %}10{% endequation %} שנמצא למעלה מספרים לנו שלושה דברים:

<ul> <li>אנחנו הולכים להשתמש במשתנה {% equation %}n{% endequation %} ולהכניס לתוכו ערכים שונים.</li>


<li>המשתנה {% equation %}n{% endequation %} <strong>מתחיל</strong> עם הערך {% equation %}1{% endequation %}.</li>


<li>המשתנה {% equation %}n{% endequation %} <strong>מסיים</strong> כשהוא מגיע לערך 10.</li>

</ul>

הרעיון הוא ש-{% equation %}n{% endequation %} מתחיל עם הערך 1, ואז מתבצעת סדרה של "צעדים" שבכל אחד מהם מגדילים את הערך של {% equation %}n{% endequation %} ב-1 בדיוק. למה ב-1? זו מוסכמה שרירותית, אבל כזו שהיא נוחה ומועילה כל כך שלא זכור לי שום מקום במתמטיקה שבו צריכים לשנות אותה.

אם כן, הביטוי {% equation %}\sum_{n=1}^{10}n^{2}{% endequation %} בעצם מתאר לנו את האלגוריתם הבא:

<ol> <li>הציבו במשתנה {% equation %}n{% endequation %} את הערך 1.</li>


<li>חשבו את {% equation %}n^{2}{% endequation %}.</li>


<li>הוסיפו את התוצאה של שלב 2 לסכום הכולל.</li>


<li>אם המשתנה {% equation %}n{% endequation %} מכיל את הערך 10, סיימו; הסכום הכולל הוא פלט החישוב.</li>


<li>אחרת, הגדילו את {% equation %}n{% endequation %} ב-1 וחזרו לשלב 2.</li>

</ol>

יש משהו אחד באלגוריתם הזה שלא באמת הוגדר - מה שאני מכנה "הסכום הכולל". מה זה? מהיכן הוא צץ? ובכן, אם אנחנו בסיבוב הראשון של החישוב אז שלב 3 צריך להיות מנוסח בצורה קצת שונה - "קבעו את הסכום הכולל להיות התוצאה של שלב 2"; רק מהאיטרציה הבאה של האלגוריתם אנחנו אמורים לומר "הוסיפו". אבל הפרדה למקרים שכזו היא עניין מעיק; איך אפשר להתחמק ממנה? הנה רעיון מאוד פשוט - נאמר שבתחילת החישוב, "הסכום הכולל" שווה ל-0. בצורה הזו לא צריך לשנות את שאר האלגוריתם.

בואו ננסח מחדש את האלגוריתם בצורה קצת יותר פורמלית כדי לקבל את הגרסה המלאה שלו. בנוסף לפורמליזם אני אעשה עוד שינוי קטן שתכף אסביר.

<ol> <li>{% equation %}S\leftarrow0{% endequation %} (הציבו 0 בסכום הכולל)</li>


<li>{% equation %}n\leftarrow1{% endequation %} (הציבו ב-{% equation %}n{% endequation %} את הערך ההתחלתי)</li>


<li>אם {% equation %}n>10{% endequation %}, סיימו; הפלט הוא {% equation %}S{% endequation %}.</li>


<li>{% equation %}S\leftarrow S+n^{2}{% endequation %} (חשבו את {% equation %}n^{2}{% endequation %} והוסיפו את התוצאה לסכום הכולל).</li>


<li>{% equation %}n\leftarrow n+1{% endequation %} (הגדילו את {% equation %}n{% endequation %} ב-1).</li>


<li>חזרו לשלב 3.</li>

</ol>

מה עוד שיניתי פה? את "תנאי העצירה" שלי - עכשיו אנחנו עוצרים אם {% equation %}n{% endequation %} הופך להיות משהו שגדול מ-10, לפני שאנחנו מספיקים להוסיף גם את המקרה הזה לסכום הכולל. למה השינוי הזה חשוב? כרגע הוא לא חשוב, אבל עוד מעט אחזור לכך.

מה שמעניין אותנו באלגוריתם הזה הוא ה<strong>גנריות</strong> שלו - את החלקים שספציפיים לסכום שלנו אפשר לשנות בקלות. אם הערך ההתחלתי של {% equation %}n{% endequation %} הוא לא 1 אלא משהו אחר רק צריך לשנות את המספר שכתוב בשלב 2; אם הערך האחרון של {% equation %}n{% endequation %} הוא לא 10 אלא משהו אחר רק צריך להחליף את ה-10 בשלב 3; ואם האיבר הכללי של הסכום הוא לא {% equation %}n^{2}{% endequation %} אלא משהו אחר רק צריך לשנות אותו בשלב {% equation %}4{% endequation %}.

אז באופן כללי יותר, אם {% equation %}f\left(n\right){% endequation %} היא פונקציה כלשהי על קלט כלשהו {% equation %}n{% endequation %}, ו-{% equation %}a,b{% endequation %} הם מספרים, אז הסכום

{% equation %}\sum_{n=a}^{b}f\left(n\right){% endequation %}

הוא תיאור קומפקטי של האלגוריתם

<ol> <li>{% equation %}S\leftarrow0{% endequation %} </li>


<li>{% equation %}n\leftarrow a{% endequation %} </li>


<li>אם {% equation %}n>b{% endequation %}, סיימו; הפלט הוא {% equation %}S{% endequation %}.</li>


<li>{% equation %}S\leftarrow S+f\left(n\right){% endequation %}</li>


<li>{% equation %}n\leftarrow n+1{% endequation %}</li>


<li>חזרו לשלב 3.</li>

</ol>

כך שאם נחזור לסכום שראינו בהתחלה, {% equation %}1+2+\ldots+10{% endequation %}, הוא פשוט נכתב בתור {% equation %}\sum_{n=1}^{10}n{% endequation %} - קצת פשוט מדי, ולכן הלכתי למשהו מסובך יותר. והנה עוד דוגמא:

{% equation %}\sum_{n=3}^{5}\frac{1}{2^{n}}=\frac{1}{8}+\frac{1}{16}+\frac{1}{32}{% endequation %}

עכשיו, כשמקבלים צעצוע חדש דחף טבעי למדי הוא לבדוק את הדרכים השונות להרוס אותו. בואו ננסה לעשות את זה עם סכום - מה קורה אם הערך שבו {% equation %}n{% endequation %} מאותחל גדול יותר מהערך שבו הוא אמור לסיים, כלומר מהו למשל {% equation %}\sum_{n=6}^{3}n^{2}{% endequation %}? אם נסתכל על האלגוריתם בגרסה החדשה שלו, נראה שבמקרה כזה בשלב 3 אנחנו מסיימים ומוציאים כפלט את {% equation %}S{% endequation %}, שרגע קודם לכן אותחל ל-0, כך ש-{% equation %}\sum_{n=6}^{3}n^{2}=0{% endequation %}. אני אוהב לומר על כך ש"סכום ריק שווה לאפס", אבל הנימוק ה"פורמלי" הוא ההגדרה שנתתי ל-{% equation %}\Sigma{% endequation %}. עכשיו, בהחלט סביר לשאול למה דבר מוזר כמו {% equation %}\sum_{n=6}^{3}n^{2}=0{% endequation %} בכלל אמור לעניין אותנו; והתשובה, כרגיל, היא שבמתמטיקה צצים המון דברים מוזרים, בפרט כשאנחנו מנסים לנסח משפט כללי מאוד ויש לו גם מקרים פרטיים פשוטים מדי שאנחנו מעדיפים לא להחריג במפורש אלא ללכת עם שיטת סימון שמטפלת גם בהם בצורה חלקה.

לפעמים אנחנו קצת משתוללים עם הסימונים. אפשר למשל לכתוב {% equation %}\sum_{1\le n\le10}n^{2}{% endequation %} וזה יהיה אותו דבר בדיוק כמו {% equation %}\sum_{n=1}^{10}n^{2}{% endequation %}. לפעמים פשוט נכתוב {% equation %}\sum_{1}^{10}n^{2}{% endequation %} מתוך הנחה שברור לקוראים שהמשתנה הרץ הוא {% equation %}n{% endequation %} (כמובן, לרוב זה מגיע בביטויים מסובכים יותר). לפעמים אפילו כותבים {% equation %}\sum n^{2}{% endequation %} בלי גבולות בכלל אם הגבולות "ברורים" מההקשר. ולפעמים לוקחים את הכלל הזה של "מוסיפים 1 בכל פעם לאינדקס" שאמרתי שהוא קדוש ומתעלמים ממנו לחלוטין, אבל בסיטואציה כזו מציינים בצורה מפורשת מה כל ערכי ה-{% equation %}n{% endequation %} הולכים להיות.

הנה דוגמא קלאסית לזה: <strong>פונקציית אוילר</strong> {% equation %}\varphi\left(n\right){% endequation %} מחזירה לכל מספר טבעי {% equation %}n{% endequation %} את מספר המספרים הטבעיים הקטנים ממנו שזרים לו, כלומר שאין להם מחלקים משותפים איתו שגדולים מ-1. הפונקציה הזו מקיימת את התכונה הנחמדה הבאה: אם סוכמים את {% equation %}\varphi\left(d\right){% endequation %} עבור כל {% equation %}d{% endequation %} שמחלק את {% equation %}n{% endequation %}, מקבלים את {% equation %}n{% endequation %} עצמו. כדי לתאר את זה בצורה פשוטה, משתמשים בסימון {% equation %}d|n{% endequation %} כדי לומר "{% equation %}d{% endequation %} מחלק את {% equation %}n{% endequation %}" (הקו האנכי אומר "מחלק"; זה סימון סטנדרטי בתורת המספרים) ואז כותבים 

{% equation %}\sum_{d|n}\varphi\left(d\right)=n{% endequation %}

כלומר, כאן הסכום רץ על כל הערכים של {% equation %}d{% endequation %} שמחלקים את {% equation %}n{% endequation %} ללא שארית.

זה מסיים את מה שיש לי להגיד על שיטת הסימון הזו ועל סכומים נחמדים במתמטיקה באופן כללי; אבל עכשיו הגיע הזמן לדבר על הסכומים הלא נחמדים - הסכומים <strong>האינסופיים</strong>. כאן העסק מתחיל להיות בעייתי יותר, ואנחנו צריכים להיות זהירים יותר, אבל זה משתלם, ממש ממש משתלם.

ובכן, מה זה אומר בעצם, סכום של <strong>אינסוף</strong> איברים? קל מאוד לתת דוגמא לסכום כזה: {% equation %}1+2+3+\ldots{% endequation %}, כלומר סכום על כל המספרים הטבעיים. אבל זה סתם סימון - כתבתי כמה סימונים ברצף, זה לא אומר שיש לזה משמעות. הרי כזכור, סכום הוא משהו שמוגדר עבור <strong>שני</strong> איברים; עבור יותר משניים ביצענו איזה שהוא <strong>תהליך</strong> שהסתיים בכך שנגמרו לי האיברים להוסיף לסכום, ואז קיבלתי כתוצאה מספר אחד ספציפי - הסכום של כל האיברים. אבל מה קורה כשיש לי אינסוף איברים? התהליך שלי פשוט לא יסתיים!

כדי לתאר סכום אינסופי אני משתמש בסימן {% equation %}\infty{% endequation %} שמתאר "אינסוף" כדי לתאר את הגבול העליון. הסימון {% equation %}\sum_{n=1}^{\infty}n^{2}{% endequation %} אומר את הדבר הבא:

<ol> <li>{% equation %}S\leftarrow0{% endequation %} (הציבו 0 בסכום הכולל)</li>


<li>{% equation %}n\leftarrow1{% endequation %} (הציבו ב-{% equation %}n{% endequation %} את הערך ההתחלתי)</li>


<li>{% equation %}S\leftarrow S+n^{2}{% endequation %} (חשבו את {% equation %}n^{2}{% endequation %} והוסיפו את התוצאה לסכום הכולל).</li>


<li>{% equation %}n\leftarrow n+1{% endequation %} (הגדילו את {% equation %}n{% endequation %} ב-1).</li>


<li>חזרו לשלב 3.</li>

</ol>

מה ההבדל בין האלגוריתם הזה לאלגוריתם שהצגתי קודם? השמטתי לחלוטין את מה שהיה שלב 3 באלגוריתם המקורי - השלב שאומר "אם {% equation %}n>b{% endequation %}, סיימו; הפלט הוא {% equation %}S{% endequation %}." במקרה הנוכחי אין "סיימנו". האלגוריתם הזה לא מסתיים ולא מוציא פלט. אז מה זה בכלל אומר?

ובכן, בשלב הזה כבר ברור שכשאנחנו מדברים על סכום אינסופי, אנחנו לא מדברים על אותו הדבר כמו סכום סופי. אבל זה לא אומר שאין קשר בין שני המושגים הללו. לפני שנביא הגדרות מפוצצות, עדיף להתחיל עם קצת אינטואיציה. נחזור אל הסכום שהראיתי בתחילת הפוסט:

{% equation %}\sum_{n=1}^{\infty}\frac{1}{2^{n}}{% endequation %}

כלומר, הסכום האינסופי {% equation %}\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\ldots{% endequation %}. הסכום הזה מככב בסיפור בכיכוב הגיבור היווני אכילס, והנה ניסוח משלי של הסיפור הזה: נניח שאכילס רוצה לרוץ מרחק של קילומטר אחד, מתחילת מסלול ריצה אל סופו. כעת, לפני שהוא יגיע אל קצה המסלול הוא בוודאי עומד לעבור בנקודת האמצע של המסלול; בשלב זה הוא עבר {% equation %}\frac{1}{2}{% endequation %} קילומטר. עכשיו, לפני שיגיע אל קצה המסלול עליו עדיין לעבור חצי מהמרחק שנותר. המרחק הכולל שנותר הוא {% equation %}\frac{1}{2}{% endequation %} קילומטר, כך שחצי מזה הוא {% equation %}\frac{1}{4}{% endequation %} קילומטר. אם כן, אכילס מגיע לנקודה הזו ועד כה עבר כבר {% equation %}\frac{1}{2}+\frac{1}{4}{% endequation %} קילומטר. כעת עליו לעבור עוד חצי מהמרחק שנותר, ולכן הוא עובר עוד {% equation %}\frac{1}{8}{% endequation %} קילומטר, וכן הלאה וכן הלאה. אם אוספים את כל המרחקים שמופיעים בסיפור שלי, יוצא שהמרחק הכולל שאכילס עובר הוא {% equation %}\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\ldots{% endequation %}. כאן אני מקווה שמתעוררת בנו <strong>האינטואיציה</strong> לפיה הסכום הזה צריך לצאת 1, כי זה המרחק הכולל שאכילס עובר בריצתו; אם אנחנו מקבלים שזו האינטואיציה, אפשר לעבור לדיון על השאלה איזה פורמליזם מתמטי יתאים לאינטואיציה הזו. אבל לא כולם מקבלים שזו האינטואיציה, ובהחלט אפשר לצעוק בשלב הזה שהסכום {% equation %}\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\ldots{% endequation %} אמור לצאת "אינסוף" כי יש בו אינסוף מחוברים.

עוד וריאציה על הסיפור של אכילס, שזכורה לי לטוב מהספר "אני שונא מתמטיקה", היא "טבלת השוקולד האינסופית". נניח שיש לנו טבלת שוקולד ואנחנו לא רוצים שתיגמר, אז בכל פעם נאכל רק חצי מהכמות שנותרה לנו. כך נאכל בפעם הראשונה {% equation %}\frac{1}{2}{% endequation %} טבלת שוקולד, בפעם השניה נאכל {% equation %}\frac{1}{4}{% endequation %} וכן הלאה. סכום כל השוקולד שנאכל הוא {% equation %}\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\ldots{% endequation %} ולכאורה הוא אמור להסתכם ל-1, כי זו טבלת השוקולד הכוללת, אבל בפועל בהחלט אפשר לומר שהסכום הזה בכלל לא מוגדר, כי זלילת טבלת השוקולד לא תסתיים אף פעם - לא משנה כמה פעמים אזלול שוקולד, עדיין יישאר משהו; זה כל הרעיון בטבלת שוקולד "אינסופית" שכזו! אבל שימו לב, כשאני שואל מה הסכום הולך לצאת, אני מתכוון - מה הוא הולך לצאת אחרי שיבוצעו כל <strong>אינסוף</strong> הצעדים? לא ברור מה זה אומר, פורמלית, אבל מה האינטואיציה פה? האינטואיציה שלי היא שאם טבלת השוקולד מספיקה לאינסוף צעדים, הרי שאחרי אותם אינסוף צעדים היא תאכל בשלמותה.

לסיפור השוקולד וגם לסיפור של אכילס יש עקב אכילס (סליחה) ברור מאוד - הם לא מציאותיים בשום צורה. עזבו שניה את אכילס, בטבלת השוקולד זה זועק לשמיים - שוקולד בסופו של דבר מורכב ממולקולות (אני אומר משהו פשטני מדי, אבל אנחנו מבינים את הקטע), ומספר המולקולות בשוקולד סופי. אי אפשר תמיד "לחלק לשתיים". בסוף תהיה לנו מולקולת שוקולד אחת ויחידה ואם נחלק אותה לשתיים, נקבל חומרים חדשים שכבר אינם שוקולד. טיעונים פיזיקליים דומים אפשר להחיל על הסיפור של אכילס. העולם הפיזי שלנו פשוט אינו אינסופי כפי שהסיפורים הללו היו רוצים.

מצד שני, המספרים הרציונליים ("השברים") הם כן אינסופיים בצורה הזו - העולם <strong>המתמטי</strong> הוא כן אינסופי, ולכן עדיף להתמקד בכך שסיפורי אכילס והשוקולד באים לתת לנו אינטואיציה, אבל הסכום {% equation %}\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\ldots{% endequation %} הוא מושג קיים גם בלי הסיפורים הללו, פשוט מעצם קיומה של המתמטיקה. ואנחנו עדיין רוצים שהוא ייצא 1.

אז מה שנעשה הוא עדיין להריץ את אלגוריתם החישוב של סכום שתיארתי קודם, אבל במקום לחכות לנצח לפלט שלא יגיע לעולם, להסתכל <strong>תוך כדי הריצה</strong> על הערכים שהסכום {% equation %}S{% endequation %} מקבל. בהתחלה הוא 0 תמיד וזה לא מעניין, אבל מה יקרה אחר כך? הוא יקבל {% equation %}\frac{1}{2}{% endequation %}, ואז הוא יקבל {% equation %}\frac{1}{2}+\frac{1}{4}=\frac{3}{4}{% endequation %}, ואז הוא יקבל {% equation %}\frac{1}{2}+\frac{1}{4}+\frac{1}{8}=\frac{7}{8}{% endequation %}, וכן הלאה וכן הלאה: אנחנו נקבל <strong>סדרה</strong> של סכומים:

{% equation %}\frac{1}{2},\frac{3}{4},\frac{7}{8},\frac{15}{16},\ldots{% endequation %}

יש חוקיות פשוטה לסדרה הזו שאפשר לתאר עם נוסחה:

{% equation %}S_{n}=\frac{2^{n}-1}{2^{n}}{% endequation %}

איך הגעתי לזה? ובכן, חישוב, אבל אפשר גם כך - אחרי שאכילס עבר {% equation %}\frac{1}{2}{% endequation %} דרך, נשארה לו עוד {% equation %}\frac{1}{2}{% endequation %} דרך; אחר כך חילקנו לשתיים את הדרך שנותרה לו. אורך כל חלק היה {% equation %}\frac{1}{4}{% endequation %}, אז החלק <strong>שנותר</strong> לאכילס אחרי השלב הזה הוא {% equation %}\frac{1}{4}{% endequation %}. אם החלק ש<strong>נותר</strong> הוא {% equation %}\frac{1}{4}{% endequation %} אז החלק שהוא כבר עבר הוא {% equation %}1-\frac{1}{4}=\frac{3}{4}{% endequation %}; באופן כללי בשלב ה-{% equation %}n{% endequation %}-י נשאר לו רק {% equation %}\frac{1}{2^{n}}{% endequation %} מהדרך, ולכן הוא עבר כבר {% equation %}1-\frac{1}{2^{n}}=\frac{2^{n}-1}{2^{n}}{% endequation %} ממנה.

לסדרת המספרים האינסופית {% equation %}S_{1},S_{2},S_{3},\ldots{% endequation %} הזו קוראים <strong>סדרת הסכומים החלקיים</strong> של הסכום {% equation %}\sum_{n=1}^{\infty}\frac{1}{2^{n}}{% endequation %}. אפשר להגדיר את זה גם באופן כללי: אם {% equation %}a_{1},a_{2},a_{3},\ldots{% endequation %} היא סדרה <strong>כלשהי</strong> של מספרים ואנו מסתכלים על הסכום האינסופי {% equation %}\sum_{i=1}^{\infty}a_{i}{% endequation %}, אז מגדירים את סדרת הסכומים החלקיים של הסכום האינסופי הזה בתור הסדרה {% equation %}S_{1},S_{2},S_{3},\ldots{% endequation %} כך ש-{% equation %}S_{n}=\sum_{i=1}^{n}a_{i}{% endequation %} (שימו לב שפתאום התחלתי להשתמש ב-{% equation %}i{% endequation %} בתור אינדקס ולא ב-{% equation %}n{% endequation %}, שבו אני משתמש לצורך אחר; כמובן שאפשר לעשות את זה, הסימון של משתנה האינדקס הוא שרירותי לגמרי).

המעבר הזה מסכום אינסופי אל סדרה אינסופית היא דוגמא ל<strong>רדוקציה</strong>; הפיכה של בעיה מסוג אחד לבעיה מסוג אחר, שאנחנו כבר יודעים לפתור. עבור סדרות אינסופיות יש מושג מאוד קונקרטי של המקום שאליו הסדרה "הולכת" שנקרא <strong>הגבול</strong> של הסדרה. זה מושג קשה לעיכול, טכנית, אבל למה שזה יעצור אותי מלנסות?

בואו נחזור שניה אל טבלת השוקולד האכילסית שלנו. ראינו שבשלב ה-{% equation %}n{% endequation %} של הזלילה, אכלנו כבר {% equation %}1-\frac{1}{2^{n}}{% endequation %} מהטבלה, כלומר מה שנשאר הוא רק {% equation %}\frac{1}{2^{n}}{% endequation %} טבלה. <strong>ההפרש</strong> בין מה שכבר אכלנו ובין המספר 1 שאנחנו <strong>מצפים</strong> שיהיה הסכום הכללי הוא ה-{% equation %}\frac{1}{2^{n}}{% endequation %} הזה. זה אומר שככל שאנחנו מתקדמים יותר ויותר בסדרה שלנו, כך ההפרש בין 1 ובין הערך הנוכחי בסדרה הולך וקטן. ההפרש הזה אף פעם לא יגיע אל אפס, אבל על מה שהוא כן עושה אנחנו אומרים במתמטית שהוא <strong>מתקרב כרצוננו לאפס</strong>.

מה זה אומר, "כרצוננו"? אפשר לחשוב על זה בתור משחק. אני מציב בפניכם "אתגר" - למשל, "תוכיחו לי שהסדרה מתישהו שתהיה במרחק מ-1 שקטן מ- {% equation %}\frac{1}{100000000}{% endequation %}". למה דווקא {% equation %}\frac{1}{100000000}{% endequation %}? ככה! שרירותי לגמרי! נמאס לי להוסיף עוד אפסים, אז עצרתי פה. 

בתגובה ל"אתגר" שלי אתם אומרים - מה הבעיה? בואו ניקח את {% equation %}n=30{% endequation %}. עבורו מתקיים {% equation %}2^{30}=1073741824{% endequation %} ו-{% equation %}1073741824>100000000{% endequation %} כך ש-{% equation %}\frac{1}{2^{n}}<\frac{1}{100000000}{% endequation %}. כלומר, האיבר {% equation %}S_{30}{% endequation %} בסדרה הוא במרחק מ-1 שקטן מ-{% equation %}\frac{1}{100000000}{% endequation %} - הצלחתם לענות על האתגר שלי.

כמובן, אני חייב לסבך את הכל. עכשיו אני אומר "אבל! אולי בהמשך הסדרה שוב מתרחקת מ-1?! לא מספיק שתראו לי שהסדרה תהיה מתישהו במרחק כזה מ-1; אני רוצה שתוכיחו לי שהחל ממקום כלשהו בסדרה, <strong>כל אברי הסדרה משם והלאה</strong> יהיו במרחק מ-1 של לכל היותר {% equation %}\frac{1}{100000000}{% endequation %}". זה ניואנס עדין, אבל הוא קריטי; למשל, אם נסתכל על הסדרה {% equation %}1,2,1,2,1,2,\ldots{% endequation %} אנחנו רואים שחצי מהאיברים שלה הם במרחק 0 מ-1, אבל לא היינו אומרים שהסדרה כולה מתקרבת אל 1.

במקרה שלנו זה לא בעייתי. נסמן {% equation %}N=30{% endequation %}. כעת אם {% equation %}n\ge N{% endequation %} אז {% equation %}2^{n}\ge2^{N}{% endequation %} ולכן {% equation %}\frac{1}{2^{n}}\le\frac{1}{2^{N}}<\frac{1}{100000000}{% endequation %} - ככל שמתקדמים בסדרה כך ההפרש רק הולך ויורד. זה לא חייב להיות כך בכל סדרה, אבל בחרתי בכוונה אחת פשוטה.

עכשיו אפשר לעבור להגדרה הכללית. ההבדל העיקרי הוא שבמקום לכתוב מספר מסורבל כמו {% equation %}\frac{1}{100000000}{% endequation %} אני אשתמש באות היוונית אפסילון, {% equation %}\varepsilon{% endequation %}. האפסילון הזה בא לתאר הגבלה על מרחק אברי הסדרה מה"יעד" שלה. אם הערך שלו יהיה שלילי זה יהיה חסר משמעות כי אין מרחקים שליליים; ואם הוא יהיה 0 זו בעצם תהיה הטענה שהחל ממקום כלשהו כל אברי הסדרה <strong>שווים</strong> ליעד שלה, וגם זו לא הסיטואציה שאנחנו רוצים לתאר. לכן אנו דורשים שיתקיים {% equation %}\varepsilon>0{% endequation %} אבל אין לנו שום דרישה אחרת - אפסילון יכול להיות "קטן כרצוננו" כל עוד הוא לא ממש אפס.

לבסוף, איך בעצם מודדים מרחק בין שני דברים? אם {% equation %}x,y{% endequation %} הם שני מספרים, המרחק ביניהם הוא {% equation %}\left|x-y\right|{% endequation %} - <strong>הערך המוחלט</strong> של ההפרש ביניהם. ערך מוחלט בהקשר שלנו הוא פשוט המספר עצמו אם הוא לא שלילי, והמינוס שלו אם הוא שלילי. כלומר {% equation %}\left|5\right|=5{% endequation %} ואילו {% equation %}\left|-5\right|=5{% endequation %}. עכשיו, משיש לנו את כל מה שנדרש, הנה ההגדרה הפורמלית של גבול של סדרה (וכאמור, זו אינה הגדרה פשוטה):

אנו אומרים ש-{% equation %}L{% endequation %} הוא <strong>הגבול </strong>של הסדרה {% equation %}a_{1},a_{2},a_{3},\ldots{% endequation %} ומסמנים זאת {% equation %}\lim_{n\to\infty}a_{n}=L{% endequation %} אם <strong>לכל</strong> {% equation %}\varepsilon>0{% endequation %} <strong>קיים</strong> {% equation %}N{% endequation %} כך ש<strong>לכל</strong> {% equation %}n>N{% endequation %} מתקיים {% equation %}\left|a_{n}-L\right|<\varepsilon{% endequation %}.

עכשיו אפשר להגדיר סוף סוף פורמלית סכום אינסופי: בהינתן {% equation %}\sum_{i=1}^{\infty}a_{i}{% endequation %} נסתכל על סדרת הסכומים החלקיים שמוגדרת באמצעות {% equation %}S_{n}=\sum_{i=1}^{n}{% endequation %}. אם קיים {% equation %}A{% endequation %} כך ש-{% equation %}\lim_{n\to\infty}S_{n}=A{% endequation %} אז <strong>נסמן</strong> {% equation %}\sum_{i=1}^{\infty}a_{i}=A{% endequation %}.

שימו לב למילת המפתח פה - <strong>אם</strong>. לא בהכרח קיים {% equation %}A{% endequation %} שהוא גבול של סדרת הסכומים החלקיים. למשל בסכום {% equation %}1+2+3+\ldots{% endequation %} שהראיתי קודם אין גבול כזה, כי הסכומים החלקיים הולכים וגדלים עוד ועוד כך שהם עוקפים כל מספר טבעי אפשרי. על סיטואציה כזו אומרים לפעמים שהסכום <strong>מתבדר לאינסוף</strong>. עוד סיטואציה שעלולה להתרחש היא שלסדרת הסכומים החלקיים לא יהיה גבול כי היא מתזזת בפראות בין שני ערכים שונים, למשל בסכום {% equation %}2-1+1-1+1-\ldots{% endequation %} סדרת הסכומים החלקיים תהיה הסדרה {% equation %}2,1,2,1,2,1,\ldots{% endequation %} שכבר הבאתי קודם בתור דוגמא לסדרה שאין לה גבול. אם כן, בניגוד לסכומים סופיים, סכום אינסופי לא בהכרח מוגדר תמיד. כשהוא כן מוגדר, אומרים שהטור <strong>מתכנס</strong>.

זו כמובן רק תחילת הסיפור. מה שהצגתי פה היא הגדרה אפשרית אחת לסכום של טורים אינסופיים. יש עוד. יש הגדרה שבה הסכום {% equation %}2-1+1-1+1-\ldots{% endequation %} יוצא {% equation %}1\frac{1}{2}{% endequation %} וזו הגדרה הגיונית ופורמלית ומוצלחת; ויש הגדרה שבה {% equation %}1+2+3+\ldots=-\frac{1}{12}{% endequation %} וגם זו הגדרה תקינה מבחינה פורמלית שיש בה יתרונות; אבל אני לא הולך לדבר עליהן כאן אבל <a href="https://gadial.net/2014/01/18/sum_of_naturals/">יש לי פוסט</a> על זה. 

נקודה מעניינת אחרת שלא אכנס לעומק שלה כי <a href="https://gadial.net/2010/04/10/riemann_series_theorem/">יש לי פוסט</a> גם עליה היא שסכום אינסופי יכול להיות תלוי בצורה קריטית ב<strong>סדר</strong> של האיברים בתוך הסכום. יש סכומים שבהם השארת <strong>אותם איברים בדיוק</strong> בסכום אבל שינוי של הסדר שבו הם מופיעים יכולים להפוך את הסכום ממתכנס למתבדר, או לגרום לו להתכנס לכל ערך מספרי שנרצה (הדוגמא הקלאסית היא הסכום {% equation %}1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\ldots{% endequation %} ואני מפרט על זה בפוסט שלי). זה מתקשר לנקודה שלי מתחילת הפוסט, שבה התעקשתי לראות סכום לא בתור "לקחת את כל שקיות התפוזים ולשפוך את כולן לקערה בבת אחת" אלא תמיד בתור <strong>תהליך</strong>. סכום אינסופי הוא יותר מאשר כלל האיברים שמופיעים בו. עבורי, הפעם הראשונה שבה שמעתי על זה שינתה לחלוטין את כל מה שחשבתי שהבנתי על מתמטיקה; בפרט, כמה האינטואיציה שלנו יכולה להטעות אותנו וכמה המתמטיקה יכולה להיות ערמומית.

אבל בשביל סיום הפוסט אני לא רוצה שנחטוף מכה לאינטואיציה, אלא ההפך - אני רוצה להראות איך מה שראינו פה מתקשר למושג שייתכן שאנחנו מכירים כבר כי ראינו אותו פה ושם, ונתקלנו בו בבית הספר, אבל לא בטוח שאי פעם הבנו אותו פורמלית עד הסוף. ואני מדבר על המספר "שליש", {% equation %}\frac{1}{3}{% endequation %}, או כמו שכותבים אותו לפעמים, {% equation %}0.333\ldots{% endequation %}.

פעם, לפני שנים רבות, הנחמה היחידה בשיעמום של שיעורי המתמטיקה בבית הספר הייתה לעשות שטויות עם המחשבון שהיה מותר לנו להביא לשיעור. אם ניסיתי לחלק 1 ב-3 במחשבון, קיבלתי תוצאה שנראית כך: {% equation %}0.33333333{% endequation %}. אחר כך כפלתי את התוצאה הזו מחדש ב-3 וקיבלתי {% equation %}0.99999999{% endequation %}, והייתה שמחה וצהלה רבה, הרי {% equation %}0.99999999{% endequation %} לא שווה ל-1, הוא רק קרוב אליו! גיליתי כשל במתמטיקה! ולפעמים, תלוי במחשבון, הייתי מקבל תוצאה עוד יותר משעשעת: {% equation %}0.33333334{% endequation %}. והמספר <strong>הזה</strong> כפול 3 היה יוצא {% equation %}1.00000002{% endequation %} - עוד יותר גדול מ-1. מה הלך פה? המחשבון ייצג את {% equation %}\frac{1}{3}{% endequation %} בייצוג <strong>עשרוני</strong>, ובייצוג כזה אי אפשר לתאר את {% equation %}\frac{1}{3}{% endequation %} במדויק עם מספר סופי של ספרות. אנחנו <strong>חייבים</strong> אינסוף ספרות כדי לתת ייצוג מדויק. הנה דוגמא לסיטואציה שבה אנחנו לא יכולים לחמוק מהאינסוף.

אבל רגע, בואו לא נרוץ קדימה מהר מדי, מה זה בכלל "ייצוג עשרוני"? כשאני כותב {% equation %}352{% endequation %}, אני בעצם כותב תרגיל חשבוני: 3 כפול מאה, ועוד 5 כפול עשר, ועוד 2 כפול 1. כלומר, אני כותב <strong>סכום</strong> שכל איבר בו הוא <strong>מקדם</strong> שמוכפל בחזקה של 10: {% equation %}352=3\times10^{2}+5\times10^{1}+2\times10^{0}{% endequation %}. הרעיון בייצוג עשרוני של שברים הוא לעשות את זה גם עם חזקות <strong>שליליות</strong> של 10; אנחנו משתמשים בנקודה העשרונית כדי להגיד מתי החזקות האי-שליליות נגמרות והחזקות השליליות מתחילות. למשל, {% equation %}0.5=5\times10^{-1}=\frac{5}{10}=\frac{1}{2}{% endequation %}, או 

{% equation %}0.125=1\times10^{-1}+2\times10^{-2}+5\times10^{-3}=\frac{125}{1000}=\frac{1}{8}{% endequation %}

עכשיו מגיע החלק המעניין - כשאנחנו כותבים מספר בייצוג עשרוני, אנחנו מרשים את האפשרות שיופיעו <strong>אינסוף</strong> ספרות מימין לנקודה העשרונית. למשל, המספר {% equation %}0.a_{1}a_{2}a_{3}\ldots{% endequation %} כאשר כל {% equation %}a_{i}{% endequation %} הוא ספרה, מייצג את הסכום

{% equation %}\sum_{n=1}^{\infty}a_{n}\times10^{-n}=\sum_{n=1}^{\infty}a_{n}\times\left(\frac{1}{10}\right)^{n}{% endequation %}

כלומר, זה סכום של <strong>חזקות</strong> של מספר קבוע כלשהו, במקרה הנוכחי {% equation %}\frac{1}{10}{% endequation %}, כשהן מוכפלות במקדמים. לסכומים כאלו יש שם מיוחד - <strong>טור חזקות</strong>. אני לא אכנס למלוא הניתוח המתמטי של טורי חזקות כאלו, אבל הנה טענה אחת: אם {% equation %}\left|q\right|<1{% endequation %} אז טור החזקות {% equation %}\sum_{n=1}^{\infty}a_{n}q^{n}{% endequation %} מתכנס תמיד. כלומר, הוא תמיד מייצג מספר, ולכן כל ייצוג עשרוני, גם כזה עם אינסוף ספרות מימין לנקודה, תמיד מייצג מספר.

נחזור כעת אל {% equation %}\frac{1}{3}{% endequation %}. אם למשל מישהו יגיד ש-{% equation %}\frac{1}{3}=0.333{% endequation %}, הטענה המדוייקת שלו תהיה ש-{% equation %}\frac{1}{3}=\frac{333}{1000}{% endequation %} וזה בוודאי לא נכון - פשוט מחשבים ורואים שאלו הם מספרים שונים. הטענה הנכונה היא ש-{% equation %}\frac{1}{3}=0.333\ldots{% endequation %}, כאשר כאן התווספו שלוש נקודות. שלוש הנקודות הללו הן קריטיות - הן אומרות "ומכאן והלאה ממשיכים כמו קודם". יש למתמטיקאים כתיב יותר פורמלי כדי לומר על מה בדיוק חוזרים שוב ושוב אבל נעזוב את זה - אנחנו מבינים את הכוונה גם ככה.

עכשיו, {% equation %}0.333\ldots=\sum_{n=1}^{\infty}\frac{3}{10^{n}}{% endequation %}. האם אני יודע לחשב את הסכום הזה? ראשית, תאמינו לי שחוקי להוציא את ה-3 החוצה, כלומר לקבל

{% equation %}\sum_{n=1}^{\infty}\frac{3}{10^{n}}=3\sum_{n=1}^{\infty}\frac{1}{10^{n}}{% endequation %}

שנית, הסכום {% equation %}\sum_{n=1}^{\infty}\frac{1}{10^{n}}{% endequation %} לא כזה שונה מהסכום {% equation %}\sum_{n=1}^{\infty}\frac{1}{2^{n}}{% endequation %} שכבר ראינו, ואני טוען שהסכום שלו יוצא {% equation %}\frac{1}{9}{% endequation %}, מה שכמובן גורר ש-

{% equation %}0.333\ldots=\sum_{n=1}^{\infty}\frac{3}{10^{n}}=3\times\frac{1}{9}=\frac{1}{3}{% endequation %}

שזה באורח פלא מה שרציתי להראות. אבל אני לא הולך לצאת מזה כל כך בקלות, נכון? אני רוצה לשכנע אתכם ש-{% equation %}\sum_{n=1}^{\infty}\frac{1}{10^{n}}=\frac{1}{9}{% endequation %} ובשביל זה אני אוכיח טענה קצת יותר כללית: {% equation %}\sum_{n=0}^{\infty}q^{n}=\frac{1}{1-q}{% endequation %} לכל {% equation %}\left|q\right|<1{% endequation %}. שימו לב שהתחלתי עכשיו את האינדקס מאפס ולא מאחד; בשביל להתחיל אותו מאחד, נשים לב שכאשר {% equation %}n=0{% endequation %} אז {% equation %}q^{n}=1{% endequation %} ולכן {% equation %}\sum_{n=0}^{\infty}q^{n}=\sum_{n=1}^{\infty}q^{n}+1{% endequation %}, כלומר:

{% equation %}\sum_{n=1}^{\infty}q^{n}=\sum_{n=0}^{\infty}q^{n}-1=\frac{1}{1-q}-1=\frac{1-\left(1-q\right)}{1-q}=\frac{q}{1-q}{% endequation %}

אם נציב {% equation %}q=\frac{1}{10}{% endequation %} בביטוי הזה, נקבל

{% equation %}\frac{1/10}{1-1/10}=\frac{1/10}{9/10}=\frac{1}{9}{% endequation %}

אז בואו נדבר על הסכום {% equation %}\sum_{n=0}^{\infty}q^{n}{% endequation %}. ליתר דיוק, בואו נסתכל על הסכום החלקי, {% equation %}S_{n}=\sum_{i=0}^{n}q^{i}{% endequation %}. יש שם לסכום הזה - <strong>סכום סדרה הנדסית</strong>. כמו הסכום {% equation %}1+2+\ldots+10{% endequation %} שבו פתחנו, ונקרא <strong>סכום סדרה חשבונית</strong>, גם לסכום סדרה הנדסית יש טריק פשוט שמאפשר לחשב אותו בקלות. הטריק הוא: להכפיל ב-{% equation %}q-1{% endequation %}!

בואו נדגים את זה עם משהו קונקרטי. נניח שאני רוצה לחשב את {% equation %}1+q+q^{2}+q^{3}{% endequation %}. אני לוקח את הסכום הזה ומשתמש בו פעמיים: פעם אחת אני כופל אותו ב-{% equation %}q{% endequation %}, ובפעם השניה אני משאיר אותו כמות שהוא, ואז אני מחסר את הסכום הראשון ומחסיר ממנו את הסכום השני. התוצאה של זה תהיה שכמעט כל האיברים הולכים <strong>להצטמצם</strong>. בואו נראה את זה. {% equation %}q{% endequation %} כפול הסכום נותן לנו את {% equation %}q+q^{2}+q^{3}+q^{4}{% endequation %}, כלומר "איבדנו" את האיבר הראשון, 1, אבל "הרווחנו" איבר חדש, {% equation %}q^{4}{% endequation %}, ושאר האיברים עדיין מופיעים בסכום. אז אנחנו מבצעים את תרגיל החיסור הבא:

{% equation %}\begin{array}{ccccccccccc}  &  &  &  & q & + & q^{2} & + & q^{3} & + & q^{4}\\ - &  & 1 & + & q & + & q^{2} & + & q^{3} \end{array}{% endequation %}

כל האיברים מצמצמים זה את זה למעט {% equation %}q^{4}{% endequation %} ו-{% equation %}1{% endequation %}, כך שאנחנו מקבלים {% equation %}q^{4}-1{% endequation %}. זה קורה גם באופן כללי:

{% equation %}\left(q-1\right)\sum_{i=0}^{n}q^{n}=q^{n+1}-1{% endequation %}

אם נחלק את שני האגפים ב-{% equation %}q-1{% endequation %}, נקבל:

{% equation %}\sum_{i=0}^{n}q^{n}=\frac{q^{n+1}-1}{q-1}{% endequation %}

כמובן, בשביל שנוכל לחלק כך חובה לדרוש ש-{% equation %}q\ne1{% endequation %}; המקרה שבו {% equation %}q=1{% endequation %} הוא פשוט במיוחד: {% equation %}\sum_{i=0}^{n}q^{n}=n+1{% endequation %}, כך שאין בעיה עם ההסתייגות הזו.

אם כן, אנחנו יודעים מה הסכם החלקי של {% equation %}\sum_{n=0}^{\infty}q^{n}{% endequation %}: זה בדיוק {% equation %}S_{n}=\frac{q^{n+1}-1}{q-1}{% endequation %}. כעת, מה קורה כאשר {% equation %}n{% endequation %} שואף לאינסוף? אפשר לפרק את הסכום הזה לשני מחוברים:

{% equation %}\frac{q^{n+1}-1}{q-1}=\frac{1}{q-1}q^{n+1}-\frac{1}{q-1}{% endequation %}

אפשר להראות שאם {% equation %}\left|q\right|<1{% endequation %} אז {% equation %}q^{n+1}{% endequation %} מתקרב לאפס כרצוננו, ולכן אפשר לקרב כרצוננו לאפס את כל {% equation %}\frac{1}{q-1}q^{n+1}{% endequation %}, מה שאומר שכאשר אנחנו בודקים מהו הגבול כאשר {% equation %}n{% endequation %} שואף לאינסוף, אפשר להשוות את כל האיבר הזה לאפס ולהישאר רק עם האיבר השני, {% equation %}-\frac{1}{q-1}{% endequation %} . אחרי שנכניס את סימן המינוס פנימה נקבל {% equation %}\frac{1}{1-q}{% endequation %} , וזה בדיוק מה שהבטחתי.

זה המקום לסיים בו את הפוסט הזה, רק נחזור אל {% equation %}\sum_{n=1}^{\infty}\frac{1}{2^{n}}=1{% endequation %} שדיברתי עליו בתחילת הפוסט. כבר ראינו שוב ושוב למה זה נכון, אבל גם הנוסחה שמצאתי עכשיו מראה את זה: ניקח את {% equation %}\frac{q}{1-q}{% endequation %} ונציב {% equation %}q=\frac{1}{2}{% endequation %} ונקבל באופן פלא {% equation %}\frac{1/2}{1-1/2}=\frac{1/2}{1/2}=1{% endequation %}. אני מקווה שהצלחתי לעמוד בהתחייבות שלי מתחילת הפוסט לגרום לנו להרגיש בנוח עם המפלצת הזו. 