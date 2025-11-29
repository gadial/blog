---
title: "אז מה זה בעצם המספרים הממשיים? (חלק ב': השדה הסדור השלם)"
layout: post
categories:
  - אנליזה מתמטית
tags:
  - מספרים ממשיים
---


<h2>מבוא</h2>

<a href="https://gadial.net/2024/08/11/real_numbers_decimal_notation/">בפוסט הקודם</a> התחלתי לדבר על המספרים הממשיים ומה הם בכלל. הראיתי את ההגדרה הנפוצה, שרובנו מכירים עוד מבית הספר, של מספר ממשי בתור משהו שיש לו פיתוח עשרוני, נאמר {% equation %}3.14159\ldots{% endequation %}. ההגדרה הזו בעצם מגדירה את המספרים הממשיים על ידי כך שהיא מדברת על האופן שבו מספר ממשי קונקרטי בנוי; אין כאן ממש התייחסות ל<strong>קבוצה</strong> של כל המספרים הממשיים.

חוץ מזה, אמרתי שההגדרה בעייתית כי את רוב המספרים הממשיים אי אפשר ממש לתאר בעולם האמיתי בעזרת פיתוח עשרוני כי לרובם המכריע אין פיתוח עשרוני שיש לנו דרך לחשב את הספרות שלו, או אפילו לתת להם הגדרה קונקרטית כלשהי - הממשיים היא קבוצה "גדולה מדי" בשביל זה. זה נותן מוטיבציה כלשהי לחיפוש אחרי הגדרה שמדברת לא על הממשי הקונקרטי אלא על <strong>המכלול</strong> שלהם, כל הקבוצה, מה בעצם הקטע שלה.

ועוד משהו בעייתי בהגדרה הזו היא שלא אמרתי בעצם מה אפשר לעשות עם המספרים הללו. מספרים הם משהו שקיים כדי שנוכל לעשות איתו דברים, ובפרט שנוכל לעשות דברים עם שני מספרים: לחבר, לחסר, להכפיל, לחלק, להשוות... אפשר לתת את ההגדרות הללו גם כשמגדירים ממשיים דרך פיתוח עשרוני, אבל זה מאלץ אותנו לנטוש את האינטואיציה הבית ספרית, ואני לא אעשה את זה כרגע.

במקום להמשיך בכיוון הזה, אני ארצה בפוסט הזה להציג את ההגדרה שאני אישית אוהב: <strong>המספרים הממשיים הם השדה הסדור השלם</strong>. כרגע אין סיבה שתבינו מה אף אחת מהמילים בהגדרה הזו אומרות, מתמטית; עד סוף הפוסט אני מקווה שנבין את כולן. אבל לפני שנתחיל צריך לתת הבהרה קטנה מה בעצם הולך בהגדרה הזו.

במתמטיקה, יש שתי דרכים מקובלות להגדיר אובייקט. דרך אחת היא לתאר במדויק מהו, כמו שעשיתי במקרה של הפיתוח העשרוני ("סדרה אינסופית של ספרות שכוללת נקודה ויכולה לכלול בהתחלה סימן מינוס"). דרך אחרת היא לתאר את האובייקט <strong>אקסיומטית</strong>. בצורה הזו לא אומרים במפורש מה האובייקט, אלא נותנים רשימה של <strong>תכונות</strong> שאנחנו מצפים שהאובייקט יקיים. התכונות הללו נקראות <strong>אקסיומות</strong>, אבל זה שונה מהשימוש במילה "אקסיומה" שהיוונים הקדמונים עשו או שאנחנו עושים בחיי היום יום. "אקסיומה" במובן היומיומי היא "משהו שאנחנו מניחים שהוא נכון בלי הוכחה". במובן המתמטי שלנו, אקסיומה היא תכונה שיכולה להתקיים עבור אובייקטים מסויימים ולא להתקיים עבור אחרים - אנחנו נראה לזה הרבה דוגמאות עוד מעט.

מרגע שיש לנו אוסף של אקסיומות, אנחנו יכולים לדבר על האובייקטים שמקיימים את <strong>כל</strong> האקסיומות. ייתכן שיש המון כאלו, ייתכן שיש רק אובייקט אחד, וייתכן שאין בכלל. במקרה של הממשיים אפשר להראות שיש לכל היותר אובייקט אחד כזה, אבל זה בפני עצמו לא אומר שהוא קיים; בנוסף להגדרה האקסיומטית נצטרך גם לתת בניה קונקרטית של הממשיים. אי אפשר להתחמק מזה. אז למה אני אוהב את ההגדרה האקסיומטית? כי היא לטעמי מה שהכי עוזר לנו להבין מה זה בעצם הממשיים, ומה התכונות שלהם. בואו נתחיל ואני מקווה שזה יתבהר בהמשך.

<h2>שדה</h2>

<h3>חזרה לבית הספר היסודי</h3>

"שדה" זה השם המפוצץ שהמתמטיקה העניקה לקבוצה שמקיימת את מה שלמדנו בבית הספר היסודי שמספרים מקיימים: יש פעולות חיבור, חיסור, כפל וחילוק ויש את חוק הקיבוץ, חוק החילוף וחוק הפילוג. את כללי החשבון אני מניח שאנחנו זוכרים (אבל יש לי <a href="https://gadial.net/2020/11/18/how_to_addition/">סדרת פוסטים</a> עליהם אם לא) אבל בואו נכתוב את החוקים במפורש:

<ul> <li>{% equation %}\left(a+b\right)+c=a+\left(b+c\right){% endequation %} (חוק הקיבוץ לחיבור)</li>


<li>{% equation %}\left(a\cdot b\right)\cdot c=a\cdot\left(b\cdot c\right){% endequation %} (חוק הקיבוץ לכפל)</li>


<li>{% equation %}a+b=b+a{% endequation %} (חוק החילוף לחיבור)</li>


<li>{% equation %}a\cdot b=b\cdot a{% endequation %} (חוק החילוף לכפל)</li>


<li>{% equation %}a\cdot\left(b+c\right)=a\cdot b+a\cdot c{% endequation %} (חוק הפילוג).</li>

</ul>

כל החוקים הללו מתקיימים יפה מאוד כבר על ידי קבוצת המספרים הטבעיים, שמסומנת ב-{% equation %}\mathbb{N}{% endequation %}. אבל {% equation %}\mathbb{N}{% endequation %} לא נקראת "שדה" כי יש דברים שחסרים. ספציפית, חיסור. החיסור חסר. אין ב-{% equation %}\mathbb{N}{% endequation %} חיסור. או, ליתר דיוק, בוודאי שיש ב-{% equation %}\mathbb{N}{% endequation %} חיסור, אבל הוא לא מוגדר עד הסוף כי אמנם {% equation %}5-2=3{% endequation %} אבל לא ממש ברור מה זה {% equation %}2-5{% endequation %} כל עוד "העולם" שלנו כולל רק את המספרים הטבעיים. אז אנחנו מרחיבים את {% equation %}\mathbb{N}{% endequation %} ומוסיפים פנימה את המספרים השליליים ואת 0 (או ש-0 כבר היה ב-{% equation %}\mathbb{N}{% endequation %}, תלוי את מי שואלים) ומקבלים את הקבוצה {% equation %}\mathbb{Z}{% endequation %}. מה שנחמד ב-{% equation %}\mathbb{Z}{% endequation %} הוא שהיא מקיימת את כל החוקים שכבר ראינו - כלומר, ההרחבה לא "עלתה" לנו באובדן של מבנה קיים, אבל אפשר לנסח בצורה נחמדה עוד חוקים בעזרתה:

<ul> <li>קיים איבר שמסומן ב-0 כך ש-{% equation %}a+0=a{% endequation %} לכל {% equation %}a{% endequation %}</li>


<li>לכל {% equation %}a{% endequation %} קיים איבר שמסומן ב-{% equation %}-a{% endequation %} ונקרא <strong>הנגדי</strong> של {% equation %}a{% endequation %} כך ש-{% equation %}a+\left(-a\right)=0{% endequation %}</li>

</ul>

בעזרת המושג הזה של "הנגדי" אפשר להגדיר חיסור בעזרת פעולת החיבור שכבר מוכרת לנו: {% equation %}a-b{% endequation %} זה בעצם {% equation %}a+\left(-b\right){% endequation %}, כלומר מחברים ל-{% equation %}a{% endequation %} את הנגדי של {% equation %}b{% endequation %}. ואם אני כבר בקטע של שמות, אז ל-0 קוראים <strong>אדיש חיבורי</strong> בהקשר הזה, כי הוא לא משפיע על מי שמתחבר איתו.

<h3>מה שנחמד בשלמים ומה שלא</h3>

אני הולך להגדיר מושג שנקרא <strong>שדה</strong> אבל שווה לעצור לרגע ולהעיר שהאקסיומות שכבר ראינו משמשות גם להגדרת מבנים אלגבריים אחרים ש-{% equation %}\mathbb{Z}{% endequation %} הוא דוגמא מרכזית אליהם. למשל, המבנה <strong>חבורה</strong> שדורש רק קיום של פעולה אחת - חיבור - ורק את חוק הקיבוץ, קיום 0 וקיום נגדי. או המבנה <strong>חוג</strong> שדורש קיום של חיבור וכפל ואת חוקי הקיבוץ וחוק הפילוג ואת קיום 0 וקיום נגדי ואת חוק החילוף לחיבור אבל <strong>לא</strong> את חוק החילוף לכפל. אני לא אזדקק למושגים הללו בהמשך אבל שווה היה לפחות להזכיר אותם.

עכשיו, האם השלמים {% equation %}\mathbb{Z}{% endequation %} הם האובייקט היחיד שמקיים את כל התכונות שראינו עד כה או שיש אחרים? התשובה היא שבהחלט יש אחרים, למשל <strong>פולינומים</strong>. הנה למשל פעולת הכפל של פולינומים: {% equation %}\left(x+3\right)\left(x+5\right)=x^{2}+8x+15{% endequation %}. קל לראות שכל התכונות שתיארתי עד כה מתקיימות גם עבור פולינומים (והדמיון שלהם ל-{% equation %}\mathbb{Z}{% endequation %} הוא למעשה גדול עד להפתיע אבל לא ניכנס לזה).

מה בכל זאת חסר ב-{% equation %}\mathbb{Z}{% endequation %} שמדרבן אותנו להמשיך הלאה? חילוק. מכיוון שחילוק הוא סוג של הפעולה ההפוכה לכפל, אפשר לקוות להגדרה שלו שתהיה דומה למה שהלך במקרה של חיבור: קודם נגדיר "אדיש כפלי", כזה שכפל בו לא משנה את התוצאה (מי זה כבר יכול להיות? נו, 1 כמובן). אחר כך נגדיר "נגדי כפלי" (אני פשוט אקרא לזה <strong>הופכי</strong>) שכפל בו מחזיר 1; ולבסוף, נגדיר חילוק במישהו בתור כפל בהופכי שלו. זה עובד לא רע, חוץ מבעיה קטנה אחת: אין ל-{% equation %}0{% endequation %} הופכי כי לא יכול להיות איבר שמכפלה שלו ב-0 מחזירה את {% equation %}1{% endequation %}. הראיתי את זה ממש לא מזמן <a href="https://gadial.net/2024/08/09/dividing_by_zero_allowed/">בפוסט שלי</a> על כך שמותר לחלק באפס בכל מני סיטואציות; ובכן <strong>עכשיו</strong> זו לגמרי <strong>לא</strong> אחת מאותן סיטואציות.

בואו ניזכר איך ההוכחה הלכה. הסתכלתי על הביטוי {% equation %}a\cdot0{% endequation %} ואז השתמשתי בכך ש-{% equation %}0=0+0{% endequation %} (כי הוא אדיש חיבורי) ולכן, על פי חוק הפילוג

{% equation %}a\cdot0=a\cdot\left(0+0\right)=a\cdot0+a\cdot0{% endequation %}

עכשיו חיסרתי את {% equation %}a\cdot0{% endequation %} משני האגפים - כלומר, חיברתי את הנגדי של {% equation %}a\cdot0{% endequation %} לשני האגפים (קיים כזה כי הנחנו שיש נגדי <strong>לכל איבר</strong> בקבוצה שלנו). כתוצאה מזה קיבלתי {% equation %}0=a\cdot0{% endequation %}, כלומר לא משנה באיזה איבר אני כופל את {% equation %}0{% endequation %}, אני אקבל 0. אבל הרי {% equation %}0\ne1{% endequation %} ולכן לא קיים {% equation %}a{% endequation %} כך ש-{% equation %}a\cdot0=1{% endequation %}.

אלא אם כן באמת מתקיים {% equation %}0=1{% endequation %}. אבל אם היה מתקיים {% equation %}0=1{% endequation %} אז על ידי כפל ב-{% equation %}a{% endequation %} בשני האגפים היינו מקבלים {% equation %}0=a{% endequation %}, כלומר הדרך היחידה שבה יתקיים {% equation %}0=1{% endequation %} תהיה אם כל הקבוצה שלנו תהיה רק {% equation %}\left\{ 0\right\} {% endequation %} ותו לא.

יודעים מה מעליב? שהקבוצה {% equation %}\left\{ 0\right\} {% endequation %} באמת מקיימת את כל הדרישות שכתבתי עד כה. והיא תקיים גם את הבאות בתור אם אני לא אדרוש במפורש {% equation %}0\ne1{% endequation %}, אז אני אדרוש את זה במפורש, ופשוט אגדיר הופכי לכל מי שאיננו 0:

<ul> <li>קיים איבר שמסומן ב-{% equation %}1{% endequation %} כך ש-{% equation %}0\ne1{% endequation %} ו-{% equation %}a\cdot1=a{% endequation %} לכל {% equation %}a{% endequation %}</li>


<li>לכל {% equation %}a\ne0{% endequation %} קיים איבר שמסומן ב-{% equation %}a^{-1}{% endequation %} ונקרא <strong>ההופכי</strong> של {% equation %}a{% endequation %} כך ש-{% equation %}a\cdot a^{-1}=1{% endequation %}</li>

</ul>

המספרים השלמים {% equation %}\mathbb{Z}{% endequation %} אמנם מקיימים את הדרישה על 1, אבל הם לא מקיימים את הדרישה על קיום הופכי. שני המספרים היחידים ב-{% equation %}\mathbb{Z}{% endequation %} שיש להם הופכי הם 1 ו-{% equation %}-1{% endequation %}; אצל שניהם הם ההופכיים של עצמם אבל באופן כללי זה לא חייב להיות ככה, כמובן.

<h3>הרציונליים נכנסים לתמונה</h3>

כדי לקבל מ-{% equation %}\mathbb{Z}{% endequation %} קבוצה שיש בה הופכי לכל מי ששונה מאפס, אנחנו מכניסים לתמונה <strong>שברים</strong>, מספרים מהצורה {% equation %}\frac{a}{b}{% endequation %} כך ש-{% equation %}b\ne0{% endequation %}, עם כללי חיבור וכפל שמכלילים את מה שאנחנו מכירים ממספרים שלמים:

<ul> <li>{% equation %}\frac{a}{b}+\frac{c}{d}=\frac{ad+bc}{bd}{% endequation %}</li>


<li>{% equation %}\frac{a}{b}\cdot\frac{c}{d}=\frac{ac}{bd}{% endequation %}</li>

</ul>

זה לא לגמרי מובן מאליו שכל התכונות שכבר ראינו עדיין מתקיימות תחת הכללים החדשים הללו, אבל לא כזה קשה לבדוק את זה. התוצאה שמתקבלת מסומנת ב-{% equation %}\mathbb{Q}{% endequation %} ואנחנו קוראים לה בדרך כל <strong>המספרים הרציונליים</strong>. אם אני רוצה לבנות <strong>פורמלית</strong> את {% equation %}\mathbb{Q}{% endequation %} (מה שאני לא עושה כאן) אני צריך קצת להיזהר כי למשל {% equation %}\frac{1}{2}=\frac{2}{4}{% endequation %}; אבל בפוסט הזה הגישה שלי היא לא לבנות שום דבר אלא רק לדבר על האקסיומות, ולראות אילו אובייקטים מקיימים אותן. והאקסיומות שתיארתי עד כה הן סוף הדרך מבחינת ההגדרה של מה זה <strong>שדה</strong>, והמספרים הרציונליים הם סוג של השדה הכי פשוט שקיים (אבל חכו עוד שניה עם זה). כדי לחדד את ההגדרה, בואו נאסוף את מה שפיזרתי לאורך החלק הזה

<strong>שדה</strong> הוא קבוצה {% equation %}F{% endequation %} עם שתי פעולות בינאריות "חיבור" {% equation %}+{% endequation %} ו"כפל" {% equation %}\cdot{% endequation %} (פעולה בינארית היא פונקציה שמקבלת זוג איברים מ-{% equation %}F{% endequation %} ומחזירה איבר ב-{% equation %}F{% endequation %}) שמקיימת את התכונות הבאות:

<ul> <li>{% equation %}\left(a+b\right)+c=a+\left(b+c\right){% endequation %}</li>


<li>{% equation %}\left(a\cdot b\right)\cdot c=a\cdot\left(b\cdot c\right){% endequation %}</li>


<li>{% equation %}a+b=b+a{% endequation %}</li>


<li>{% equation %}a\cdot b=b\cdot a{% endequation %} </li>


<li>{% equation %}a\cdot\left(b+c\right)=a\cdot b+a\cdot c{% endequation %}</li>


<li>קיים איבר שמסומן ב-0 כך ש-{% equation %}a+0=a{% endequation %} לכל {% equation %}a{% endequation %}</li>


<li>לכל {% equation %}a{% endequation %} קיים איבר שמסומן ב-{% equation %}-a{% endequation %} ונקרא <strong>הנגדי</strong> של {% equation %}a{% endequation %} כך ש-{% equation %}a+\left(-a\right)=0{% endequation %}</li>


<li>קיים איבר שמסומן ב-{% equation %}1{% endequation %} כך ש-{% equation %}0\ne1{% endequation %} ו-{% equation %}a\cdot1=a{% endequation %} לכל {% equation %}a{% endequation %}</li>


<li>לכל {% equation %}a\ne0{% endequation %} קיים איבר שמסומן ב-{% equation %}a^{-1}{% endequation %} ונקרא <strong>ההופכי</strong> של {% equation %}a{% endequation %} כך ש-{% equation %}a\cdot a^{-1}=1{% endequation %}</li>

</ul>

תשע האקסיומות הללו הן כל מה שיש; מתוכן אפשר להסיק כללים אחרים שמוכרים לנו, כמו למשל הכלל שכפל של משהו ב-0 תמיד מחזיר 0. 

בואו נוכיח עוד תכונה לדוגמא: שהאדיש החיבורי הוא יחיד. כלומר שאין איזה איבר {% equation %}0^{\prime}\ne0{% endequation %} כך ש-{% equation %}a+0^{\prime}=a{% endequation %} לכל {% equation %}a{% endequation %}. ההוכחה היא די טריוויאלית, כי אם נניח שיש {% equation %}0^{\prime}{% endequation %} כך ש-{% equation %}a+0^{\prime}=a{% endequation %} <strong>לכל</strong> {% equation %}a{% endequation %} אז זה בפרט נכון עבור {% equation %}a=0{% endequation %}, ואז {% equation %}0+0^{\prime}=0{% endequation %} (כי {% equation %}0^{\prime}{% endequation %} אדיש) אבל גם {% equation %}0+0^{\prime}=0^{\prime}{% endequation %} (כי {% equation %}0{% endequation %} אדיש) וקיבלנו {% equation %}0=0^{\prime}{% endequation %}.

הנה משהו יותר טריקי באותה רוח: אני רוצה להראות שלא סתם אין אדיש נוסף, אלא שאפילו אם נבחר איבר {% equation %}a{% endequation %} ספציפי כלשהו, אין מישהו נוסף שמשמש כאדיש <strong>עבורו</strong>. כלומר, אם {% equation %}x{% endequation %} הוא איבר כלשהו כך ש-{% equation %}a+x=a{% endequation %} אז {% equation %}x=0{% endequation %}. על פניו גם זה טריוויאלי: בואו פשוט נעביר את {% equation %}a{% endequation %} אגף ונקבל {% equation %}x=0{% endequation %}. אבל בואו נעשה את זה לאט, כדי שנבין באילו כללים אנחנו משתמשים:

{% equation %}a+x=a{% endequation %} (זו נקודת המוצא שלנו)

{% equation %}-a+\left(a+x\right)=-a+a{% endequation %} (חיברנו {% equation %}-a{% endequation %} לשני האגפים; שימו לב ששמתי סוגריים על {% equation %}a+x{% endequation %} מאגף שמאל כדי להדגיש שפעולת החיבור שלהם "מתבצעת קודם")

{% equation %}\left(-a+a\right)+x=-a+a{% endequation %} (על אגף שמאל השתמשתי בחוק הקיבוץ לחיבור)

{% equation %}\left(a+\left(-a\right)\right)+x=a+\left(-a\right){% endequation %} (על שני האגפים השתמשתי בחוק החילוף לחיבור)

{% equation %}0+x=0{% endequation %} (השתמשתי בכך שאיבר ועוד הנגדי שלו זה 0)

{% equation %}x+0=0{% endequation %} (עוד שימוש בחוק החילוף לחיבור)

{% equation %}x=0{% endequation %} (סיימנו)

שימו לב לרמת הפדנטיות שלי: אני לא אומר {% equation %}0+x=x{% endequation %} ישירות, כי בניסוח שלי של מהו 0 אמרתי רק ש-{% equation %}a+0=a{% endequation %} לכל {% equation %}a{% endequation %}. הסיבה לכך שהגדרתי 0 ככה היא שידעתי שיהיה לי את חוק החילוף; אם חוק החילוף לא היה מובטח לי, הייתי מגדיר את האדיש בתור מישהו שמקיים {% equation %}a+0=0+a=a{% endequation %} (ואכן, אם תסכלו בהגדרות של תורת החבורות, איפה שכללי החילוף לא מובטחים, כך מגדירים).

הנה עוד משהו באותו רוח - לכל {% equation %}a{% endequation %}, הנגדי של {% equation %}a{% endequation %} הוא יחיד. כלומר אם {% equation %}a+x=0{% endequation %} וגם {% equation %}a+y=0{% endequation %} אז {% equation %}x=y{% endequation %}. את זה קל למדי להראות: מכך ש-{% equation %}a+x=0=a+y{% endequation %} נסיק {% equation %}a+x=a+y{% endequation %} ועכשיו נחבר את {% equation %}-a{% endequation %} לשני האגפים, נשתמש בחוק הקיבוץ ונקבל {% equation %}x=y{% endequation %}.

בעזרת יחידות הנגדי אני אוכיח עוד תכונה מעניינת במיוחד: {% equation %}\left(-a\right)\cdot\left(-b\right)=ab{% endequation %}, כלומר "מינוס כפול מינוס זה פלוס". <a href="https://gadial.net/2017/07/30/minus_minus/">יש לי פוסט</a> שמנסה להסביר את האינטואיציה מאחורי זה, אבל עכשיו אנחנו לא זקוקים לאינטואיציה - יש לנו <strong>אקסיומות</strong> ואפשר <strong>להוכיח</strong> מהן דברים.

ראשית, בואו נראה ש-{% equation %}-a=\left(-1\right)\cdot a{% endequation %}. במילים: הנגדי של {% equation %}a{% endequation %} שווה לנגדי של 1 כפול {% equation %}a{% endequation %}. כדי להראות את זה בואו נסתכל על הסכום {% equation %}\left(-1\right)\cdot a+a{% endequation %}. נשתמש בחוק הפילוג ונקבל

{% equation %}\left(-1\right)\cdot a+a=\left(-1+1\right)\cdot a=0\cdot a=0{% endequation %}

ולכן קיבלנו ש-{% equation %}\left(-1\right)\cdot a{% endequation %} הוא באמת הנגדי של {% equation %}a{% endequation %}, תוך שאנחנו משתמשים במובלע בזה שהנגדי הוא <strong>יחיד</strong>.

<h3>עוד דוגמאות לשדות ובפרט שדות סופיים</h3>

עכשיו בואו נדבר על עוד שדות. מבית הספר אנחנו מכירים את הממשיים {% equation %}\mathbb{R}{% endequation %} שמכילים את {% equation %}\mathbb{Q}{% endequation %}, ואולי מכירים גם את המרוכבים {% equation %}\mathbb{C}{% endequation %} שמכילים את {% equation %}\mathbb{R}{% endequation %}: כולם שדות, אבל מכיוון שאני מנסה בפוסטים הללו להגדיר את {% equation %}\mathbb{R}{% endequation %} אולי לא נלך לכיוון של הדוגמאות האלו. האם יש עוד דברים? האמת היא שיש <strong>המון</strong> שדות. הנה דוגמא פשוטה: אנחנו יודעים ששורש 2 הוא לא מספר רציונלי, מה שמסומן ב-{% equation %}\sqrt{2}\notin\mathbb{Q}{% endequation %} (יש לי הסבר <a href="https://gadial.net/2008/10/31/irrationality_of_square_roots/">כאן</a>). אז אני יכול "לצרף" אותו ל-{% equation %}\mathbb{Q}{% endequation %} במובן הבא: אני יוצר קבוצה {% equation %}\mathbb{Q}\left(\sqrt{2}\right)=\left\{ a+b\sqrt{2}\ |\ a,b\in\mathbb{Q}\right\} {% endequation %}. איברים טיפוסיים של הקבוצה הם {% equation %}\sqrt{2}{% endequation %} ו-{% equation %}3-5\sqrt{2}{% endequation %} וגם {% equation %}17{% endequation %}. עכשיו, פעולות החיבור והכפל של איברים בקבוצה יתנהגו באופן המתבקש:

<ul> <li>{% equation %}\left(a+b\sqrt{2}\right)+\left(c+d\sqrt{2}\right)=\left(a+c\right)+\left(b+d\right)\sqrt{2}{% endequation %}</li>


<li>{% equation %}\left(a+b\sqrt{2}\right)\cdot\left(c+d\sqrt{2}\right)=\left(ac+2bd\right)+\left(bc+ad\right)\sqrt{2}{% endequation %}</li>

</ul>

לא קשה לראות שתחת ההגדרות הללו, קיבלנו ש-{% equation %}\mathbb{Q}\left(\sqrt{2}\right){% endequation %} היא שדה. מכיוון שאפשר היה לעשות את המשחק הזה עם כל שורש של כל מספר רציונלי (וגם עם מספרים טיפה יותר מסובכים) אנחנו מקבלים פה בעצם עושר אדיר של שדות. יש תחום שלם - <strong>תורת השדות</strong> - שמתעסק בשדות הללו ובבלאגן העצום שלהם; זה התחום שבו מוכיחים <a href="https://gadial.net/2018/04/16/field_theory_straightedge_and_compass/">שלבעיות הבניה בסרגל ומחוגה של היוונים הקדמונים אין פתרון</a>, <a href="https://gadial.net/2018/07/12/insolvability_of_the_quintic/">ושאין נוסחה לפתרון משוואה ממעלה חמישית ומעלה</a>, אבל אני לא אדבר על זה כאן (והמתמטיקה המעורבת היא מסובכת יחסית, אם כי עדיין ברמה של תואר ראשון).

בואו נעבור לראות עוד שדות, פשוטים יותר. קודם ראינו שבאופן מעליב משהו, הקבוצה {% equation %}\left\{ 0\right\} {% endequation %} היא כמעט שדה - הסיבה היחידה שהיא לא הייתה שדה היא הדרישה המפורשת שלנו ש-{% equation %}0\ne1{% endequation %}. אם כן, מה עם {% equation %}\left\{ 0,1\right\} {% endequation %}? האם הקבוצה הזו היא כן שדה? לכאורה לא, כי פעולת החיבור מוציאה אותנו מגבולות השדה: {% equation %}1+1=2{% endequation %}. אבל נניח שהיינו <strong>רוצים</strong> שהקבוצה הזו תהיה שדה, איך היינו צריכים "לתקן" את פעולת החיבור? ובכן, אפשר להגדיר או {% equation %}1+1=1{% endequation %} או {% equation %}1+1=0{% endequation %}. אבל ההגדרה הראשונה מובילה, אחרי העברת אגפים אל {% equation %}1=0{% endequation %} שכבר אמרנו שאסור. לעומת זאת ההגדרה {% equation %}1+1=0{% endequation %} היא מצוינת; היא לא גורמת לשום בעיות. עם ההגדרה הזו, {% equation %}\left\{ 0,1\right\} {% endequation %} היא <strong>באמת</strong> שדה, שבדרך כלל מסומן בתור {% equation %}\mathbb{Z}_{2}{% endequation %} או {% equation %}\mathbb{F}_{2}{% endequation %} ותכף נבין את הניואנס שמבדיל בין הסימונים.

אם כן, {% equation %}\mathbb{F}_{2}{% endequation %} הוא השדה הזעיר ביותר שקיים. בפרט יש בו מספר <strong>סופי</strong> של איברים, להבדיל מ-{% equation %}\mathbb{Q}{% endequation %} האינסופי. האם יש עוד שדות שדומים ל-{% equation %}\mathbb{F}_{2}{% endequation %}? נראה די מתבקש להסתכל על הקבוצה {% equation %}\mathbb{Z}_{3}=\left\{ 0,1,2\right\} {% endequation %}. ושוב, אנחנו נתקלים בבעיה כשאנחנו מסתכלים על {% equation %}1+1+1{% endequation %} שלא יכול להיות שווה 3. הוא גם לא יכול להיות שווה 1 כי מ-{% equation %}1+1+1=1{% endequation %} נקבל {% equation %}2=0{% endequation %} ואז אין לנו שלושה איברים; והוא לא יכול להיות 2 כי אז {% equation %}1+1+1=2{% endequation %} יגרור {% equation %}1=0{% endequation %} כמו קודם; לכן אנחנו מגדירים {% equation %}1+1+1=0{% endequation %}. 

מההגדרה הזו עולה גם מה אמור לצאת {% equation %}2\cdot2{% endequation %}, כי הרי {% equation %}2=1+1{% endequation %} אז אפשר להשתמש בחוק הפילוג ולקבל {% equation %}2\cdot2=\left(1+1\right)\left(1+1\right)=1+1+1+1=1{% endequation %}. מה שקורה כאן בפועל הוא שב-{% equation %}\mathbb{Z}_{3}{% endequation %} אנחנו נדחפים להגדיר את פעולות החיבור והכפל <strong>מודולו </strong><strong>3</strong>. כלומר - מבצעים חיבור או כפל רגילים, אבל אחר כך מחלקים את התוצאה ב-3 ולוקחים רק את השארית. בגלל ש-{% equation %}1+1+1{% endequation %} מתחלק ב-3, השארית יוצאת 0 ולכן אנחנו מקבלים את השוויון {% equation %}1+1+1=0{% endequation %} שממנו אפשר להסיק גם במקרה של {% equation %}2\cdot2{% endequation %}. עם ההגדרות הללו, {% equation %}\mathbb{Z}_{3}{% endequation %} היא באמת שדה, שמסומן {% equation %}\mathbb{F}_{3}{% endequation %}.

את הרעיון הזה אפשר להכליל לכל מספר טבעי {% equation %}n{% endequation %}: מסמנים ב-{% equation %}\mathbb{Z}_{n}{% endequation %} את הקבוצה {% equation %}\left\{ 0,1,2,\ldots,n-1\right\} {% endequation %} של כל המספרים הטבעיים מאפס עד {% equation %}n-1{% endequation %}; אם חושבים על זה רגע, זו קבוצת כל השאריות האפשריות שמתקבלות כשמחלקים מספר טבעי כלשהו ב-{% equation %}n{% endequation %}. פעולות החיבור והכפל מוגדרות על הקבוצה הזו כמו על מספרים טבעיים רגילים, אבל אחרי קבלת התוצאה מחלקים ב-{% equation %}n{% endequation %} ולוקחים את השארית. לא קשה לראות ש-{% equation %}\mathbb{Z}_{n}{% endequation %} הזו מקיימת את רוב התכונות היפות שדיברנו עליהן: חוקי הקיבוץ, החילוף והפילוג; קיום אדיש חיבורי (0) וקיום נגדי לכל איבר (הנגדי של {% equation %}a\ne0{% endequation %} הוא {% equation %}n-a{% endequation %} והנגדי של 0 הוא 0); וקיום אדיש כפלי (1). אבל {% equation %}\mathbb{Z}_{n}{% endequation %} הוא <strong>לא</strong> בהכרח שדה, והדוגמא הראשונה היא {% equation %}\mathbb{Z}_{4}{% endequation %}. 

הבעיה הבסיסית ב-{% equation %}\mathbb{Z}_{4}{% endequation %} היא ש-{% equation %}2\cdot2=0{% endequation %}, מה שמבטיח של-{% equation %}2{% endequation %} לא יכול להיות הופכי, כי נניח שהיה {% equation %}x{% endequation %} כלשהו כך ש-{% equation %}2x=1{% endequation %}, אז היינו כופלים את {% equation %}2\cdot2=0{% endequation %} ב-{% equation %}x{% endequation %} משני האגפים ומקבלים 

{% equation %}0=0\cdot x=2\cdot2x=2{% endequation %}

כלומר {% equation %}0=2{% endequation %}, מה שאנחנו מניחים שלא מתקיים. זו תוצאה שנכונה לא ל-2 אלא באופן כללי במבנה שקראתי לו <strong>חוג</strong>: אומרים ש-{% equation %}a,b{% endequation %} הם <strong>מחלקי אפס</strong> אם {% equation %}ab=0{% endequation %} למרות ש-{% equation %}a\ne0{% endequation %} וגם {% equation %}b\ne0{% endequation %}, ואפשר להוכיח בדיוק באותו אופן שראינו שמחלקי אפס לא יכולים להיות הפיכים. 

כדי ש-{% equation %}\mathbb{Z}_{n}{% endequation %} יהיה שדה, הכרחי שלא יהיו בו מחלקי אפס. מכיוון שאם יש {% equation %}a,b>0{% endequation %} כך ש-{% equation %}n=ab{% endequation %} אז {% equation %}a,b{% endequation %} כן יהיו מחלקי אפס, תנאי הכרחי לכך ש-{% equation %}\mathbb{Z}_{n}{% endequation %} יהיה שדה הוא ש-{% equation %}n{% endequation %} יהיה <strong>ראשוני</strong>. <a href="https://gadial.net/2013/05/13/modular_arithmetic/">לא קשה להראות</a> שזה גם תנאי <strong>מספיק</strong>, כלומר שאם {% equation %}p{% endequation %} ראשוני אז {% equation %}\mathbb{Z}_{p}{% endequation %} הוא שדה, ובמקרה הזה מסמנים את השדה ב-{% equation %}\mathbb{F}_{p}{% endequation %}. הנה הניואנס המדובר: {% equation %}\mathbb{Z}_{n}{% endequation %} הוא סימון כללי עבור <strong>החוג</strong> שמשתמשים בו גם כשהחוג אינו שדה, אבל ב-{% equation %}\mathbb{F}_{n}{% endequation %} משתמשים רק כשהוא שדה.

אם כן, קיבלנו עכשיו עושר של שדות חדשים: {% equation %}\mathbb{F}_{p}{% endequation %} לכל אחד מאינסוף הראשוניים {% equation %}p{% endequation %} הקיימים. בניגוד ל-{% equation %}\mathbb{Q}{% endequation %} כל השדות הללו הם <strong>סופיים</strong>. האם אלו כל השדות הסופיים? ובכן, לא, אבל זו נקודת התחלה טובה. אפשר להוכיח שלכל מספר ראשוני {% equation %}p{% endequation %} ולכל מספר טבעי {% equation %}n{% endequation %} קיים שדה אחד ויחיד עם {% equation %}p^{n}{% endequation %} איברים, שמסומן {% equation %}\mathbb{F}_{p^{n}}{% endequation %}, והשדה הזה מכיל את {% equation %}\mathbb{F}_{p}{% endequation %} בתור תת-קבוצה. 

איך בדיוק {% equation %}\mathbb{F}_{p^{n}}{% endequation %} נראה? זה טיפה טריקי: אפשר לחשוב על אברי {% equation %}\mathbb{F}_{p^{n}}{% endequation %} בתור <strong>פולינומים</strong> ממעלה קטנה מ-{% equation %}n{% endequation %} שהמקדמים שלהם שייכים ל-{% equation %}\mathbb{F}_{p}{% endequation %}, למשל אפשר לחשוב על אברי {% equation %}\mathbb{F}_{7^{3}}{% endequation %} בתור פולינומים כמו {% equation %}2x+5{% endequation %} ו-{% equation %}6x^{2}+2{% endequation %} ופעולת החיבור מוגדרת באופן הסטנדרטי עבור פולינומים, כך שבדוגמא שלי {% equation %}\left(6x^{2}+2\right)+\left(2x+5\right)=6x^{2}+2x+7=6x^{2}+2x{% endequation %} (ה-{% equation %}7{% endequation %} נעלם כי החיבור הוא מודולו 7 כי המקדמים של הפולינום הם איברים של {% equation %}\mathbb{F}_{7}{% endequation %}). אבל כפל הוא לא כזה פשוט. הרעיון הוא שכופלים את הפולינומים, ואז מחלקים את התוצאה <strong>בפולינום</strong> ספציפי ממעלה {% equation %}n{% endequation %} מעל {% equation %}\mathbb{F}_{p}{% endequation %} שנבחר מראש. כדי שזה יעבוד ונקבל שדה הפולינום הזה צריך להיות <strong>אי פריק</strong> אבל אני גולש פה כבר לנושא לא קשור - <a href="https://gadial.net/2011/07/14/finite_fields_intro/">הנה פוסט שלי</a> שמתעסק בשדות סופיים ונכנס לפרטים הללו.

לסיום, בואו נעניק שם מפורש למושג המובלע שהשתמשנו בו בחלק הזה. אנחנו אומרים ש<strong>המציין</strong> של השדה {% equation %}\mathbb{F}{% endequation %} הוא {% equation %}n{% endequation %} אם לחבר את 1 לעצמו {% equation %}n{% endequation %} פעמים מחזיר 0 אבל כל חיבור של 1 לעצמו מספר קטן יותר של פעמים הוא לא 0. למשל, המציין של {% equation %}\mathbb{F}_{7}{% endequation %} הוא 7. כבר ראינו שהמציין של שדה חייב להיות מספר ראשוני, אם הוא קיים; אם לא משנה כמה פעמים נחבר את 1 לעצמו, תמיד נקבל משהו שונה מאפס, אומרים שהמציין של השדה הוא 0 (למשל, המציין של {% equation %}\mathbb{Q}{% endequation %} הוא 0).

עכשיו כשאנחנו כבר מבינים פחות או יותר מה זה שדה, מה מפריד שדות מדברים דומים שאינם שדות, ויש לנו כמה דוגמאות קונקרטיות לשדות ובפרט {% equation %}\mathbb{Q}{% endequation %} והשדות {% equation %}\mathbb{F}_{p}{% endequation %}, אפשר להתקדם הלאה ולעבור אל עוד אקסיומות שאפשר להוסיף לשדה והן פחות נפוצות באלגברה אבל סופר-שימושיות בחשבון דיפרנציאלי ואינטגרלי: אקסיומות <strong>סדר</strong>.

<h2>סדור</h2>

<h3>מה זה "מספר חיובי"?</h3>

כשאנחנו כותבים {% equation %}3<5{% endequation %} אנחנו יודעים למה אנחנו מתכוונים: 5 גדול מ-3. הוא בא "אחריו" בסדר של המספרים. אנחנו הרי סופרים ככה: אחת, שתיים, שלוש, ארבע, חמש. שלוש בא קודם, חמש אחר כך, אז זה מסומן קומפקטית ב-{% equation %}3<5{% endequation %}. אז אינטואיציה יש, אבל איך מגדירים את זה <strong>פורמלית</strong>?

ההגדרה ה"סדרתית" לא תביא אותנו יותר מדי רחוק אם יש לנו שאיפות גדולות יותר מאשר לדבר על הטבעיים. אנחנו רוצים הגדרה שיהיה בה הגיון בהרבה שדות, למשל ב-{% equation %}\mathbb{Q}{% endequation %}. יש לנו את האינטואיציה לכך ש-{% equation %}\frac{1}{2}<\frac{3}{4}{% endequation %}, אבל איך זה מוגדר פורמלית? לנסות לסדר את השברים בסדרה כמו שעשינו עם הטבעיים זה כאב ראש שלא ייאמן (נסו!) אבל למרבה המזל יש לנו טריק פשוט מאוד: פשוט נסתכל על {% equation %}\frac{3}{4}-\frac{1}{2}{% endequation %} ונשאל את עצמנו - האם זה מספר <strong>חיובי</strong> או <strong>שלילי</strong>?

כמובן, במבט ראשון לא פתרנו הרבה כי מה זה בכלל "מספר חיובי"? ההגדרה הפשוטה היא - מספר {% equation %}a{% endequation %} הוא חיובי אם {% equation %}0<a{% endequation %}, כלומר אני מגדיר חיוביים בעזרת הסימן {% equation %}<{% endequation %} של "גדול מ-". אבל היופי בעניין הוא שאני <strong>לא צריך</strong> את הסימן הזה כדי להגדיר חיובי. מלכתחילה אני קורא למספרים הטבעיים (בלי אפס) "החיוביים" ולנגדיים שלהם "השליליים", אז אני יכול להתבסס על הדיכוטומיה הזו כדי להגדיר את {% equation %}<{% endequation %} מלכתחילה.

זה נשמע קצת רעוע, אני מודה, אבל היופי פה שזה באמת עובד, וכדי לראות כמה טוב זה עובד אני אעשה את זה על שדה כללי, עם הגדרות אבסטרקטיות, ונראה כמה רחוק אפשר להגיע.

הרעיון הוא זה: נניח ש-{% equation %}\mathbb{F}{% endequation %} הוא שדה כלשהו. עכשיו אנחנו מגדירים עליו מבנה חדש באמצעות קבוצה {% equation %}P\subseteq\mathbb{F}{% endequation %} שאנחנו קוראים לאיברים שלה <strong>חיוביים</strong>. כדי שדברים יעבדו כמו שאנחנו מצפים, אנחנו דורשים שלוש אקסיומות מה"חיוביים" הללו:

<ul> <li>לכל {% equation %}a\in\mathbb{F}{% endequation %} בדיוק אחד מהבאים מתקיים: או ש-{% equation %}a\in P{% endequation %}, או ש-{% equation %}-a\in P{% endequation %}, או ש-{% equation %}a=0{% endequation %}.</li>


<li>אם {% equation %}a,b\in P{% endequation %} אז {% equation %}a+b\in P{% endequation %}</li>


<li>אם {% equation %}a,b\in P{% endequation %} אז {% equation %}a\cdot b\in P{% endequation %}</li>

</ul>

זה הכל! האקסיומה הראשונה אומרת "כל איבר שונה מאפס הוא או חיובי או שלילי". שתי האחרות אומרות "סכום ומכפלה של חיוביים הוא חיובי". אלו בבירור תכונות שאנחנו מצפים מחיוביים לקיים ומתקיימות עבור {% equation %}\mathbb{N}{% endequation %}; מה שנראה קצת הזוי פה הוא שזה מספיק כדי להגדיר את יחס הסדר {% equation %}<{% endequation %} ולהסיק את כל התכונות שלו, אבל למרבה השמחה זה בדיוק מה שקורה, ואנחנו קוראים בשם <strong>שדה סדור</strong> לשדה {% equation %}\mathbb{F}{% endequation %} עם תת-קבוצה {% equation %}P{% endequation %} שמקיימת את האקסיומות הללו.

בתור התחלה, בואו נשים לב ש-{% equation %}1{% endequation %} הוא תמיד חיובי, לא משנה כמה מוזר ננסה ש-{% equation %}P{% endequation %} תהיה. מכיוון ש-{% equation %}0\ne1{% endequation %} יש ל-1 בדיוק שתי ברירות: או ש-{% equation %}1\in P{% endequation %} או ש-{% equation %}-1\in P{% endequation %}. אבל זכרו שראינו שמינוס כפול מינוס הוא פלוס (ואת זה ראינו עוד לפני שהתחלנו לדבר על חיוביים ושליליים!) אז אם {% equation %}-1\in P{% endequation %}, מהאקסיומה על כפל נקבל ש-{% equation %}1=\left(-1\right)\cdot\left(-1\right)\in P{% endequation %}, בסתירה להנחה ש-{% equation %}-1\in P{% endequation %}. אז המסקנה שלנו היא ש-{% equation %}1\in P{% endequation %} ואילו {% equation %}-1\notin P{% endequation %}, כלומר 1 הוא תמיד חיובי ו-{% equation %}-1{% endequation %} הוא תמיד שלילי. עכשיו אפשר להשתמש בסגירות של {% equation %}P{% endequation %} לחיבור כדי לקבל שבכל שדה סדור, כל האיברים מהצורה {% equation %}n{% endequation %} (חיבור של {% equation %}1{% endequation %} לעצמו {% equation %}n{% endequation %} פעמים) הם חיוביים וכל האיברים מהצורה {% equation %}-n{% endequation %} הם שליליים. במילים אחרות, כל שדה סדור ממציין 0 מכיל עותק של {% equation %}\mathbb{Z}{% endequation %} ששומר על המשמעות המקורית של "חיוביים" ו"שליליים" ב-{% equation %}\mathbb{Z}{% endequation %}.

ההגדרה של {% equation %}P{% endequation %} השתמשה בצורה מהותית באיברים נגדיים, אבל מה עם איברים הופכיים? אם {% equation %}a\in P{% endequation %}, האם גם {% equation %}a^{-1}\in P{% endequation %}? התשובה חיובית. ראשית שימו לב ש-{% equation %}a^{-1}{% endequation %} בכלל מוגדר; אם היה מתקיים {% equation %}a=0{% endequation %} הוא לא היה מוגדר, אבל {% equation %}a\in P{% endequation %} ולכן {% equation %}a\ne0{% endequation %}. שנית, בגלל ש-{% equation %}a^{-1}\ne0{% endequation %} מאותו נימוק, אז או ש-{% equation %}a^{-1}\in P{% endequation %} או ש-{% equation %}-a^{-1}\in P{% endequation %}. בואו נניח בשלילה שדווקא המקרה השני מתקיים, אז בגלל שגם {% equation %}a\in P{% endequation %} נקבל {% equation %}-1=\left(-a^{-1}\right)\cdot a\in P{% endequation %} וזו סתירה, לכן {% equation %}a^{-1}\in P{% endequation %}.

התוצאה שזה עתה ראיתי מאפשרת לי לדבר על {% equation %}\mathbb{Q}{% endequation %}. כזכור, כל שדה ממציין 0 מכיל יותר מאשר עותק של {% equation %}\mathbb{Z}{% endequation %} - הוא מכיל עותק של {% equation %}\mathbb{Q}{% endequation %}; האם גם בו נשמרת המשמעות המקורית של "חיוביים" ו"שליליים"? כל מספר רציונלי ניתן לכתיבה בתור {% equation %}\frac{a}{b}{% endequation %}, שזו דרך אחרת לכתוב את הביטוי {% equation %}a\cdot b^{-1}{% endequation %} שמשתמש ישירות באקסיומות השדה. כך ש-{% equation %}b\ne0{% endequation %}. אם {% equation %}a=0{% endequation %} אז {% equation %}\frac{a}{b}=0{% endequation %}. אחרת, אם {% equation %}a\in P{% endequation %} וגם {% equation %}b\in P{% endequation %} אז {% equation %}b^{-1}\in P{% endequation %} ממה שראינו ולכן {% equation %}ab^{-1}\in P{% endequation %}. באופן דומה, אם {% equation %}-a,-b\in P{% endequation %} נקבל שוב {% equation %}\frac{a}{b}\in P{% endequation %} ואילו אם {% equation %}a,-b\in P{% endequation %} או {% equation %}-a,b\in P{% endequation %} נקבל ש-{% equation %}-ab^{-1}\in P{% endequation %} . זה תואם את המשמעות הרגילה של חיוביים והשליליים עבור הרציונליים.

מה עם שדות שהם לא ממציין 0, למשל {% equation %}\mathbb{F}_{5}{% endequation %}? באופן די מובהק פשוט <strong>לא ניתן</strong> להגדיר עליהם סדר. כי אם {% equation %}\mathbb{F}{% endequation %} הוא שדה ממציין {% equation %}n{% endequation %}, אז מצד אחד {% equation %}1,n-1{% endequation %} שניהם חיוביים ממה שכבר ראינו, אבל אז גם {% equation %}1+\left(n-1\right){% endequation %} צריך להיות חיובי - אבל הוא יוצא 0, ו-0 הוא לא חיובי. אז מלכתחילה כשאנחנו מדברים על "שדה סדור" אנחנו מתכוונים לשדה ממציין 0 (ובפרט, אין שדה סדור סופי).

<h3>איך מגדירים סדר וערך מוחלט בעזרת החיוביים</h3>

עכשיו בואו נשתמש בחיוביים והשליליים כדי להגדיר יחס סדר {% equation %}<{% endequation %}, ונעשה את זה על פי הרעיון האינטואיטיבי שכבר ראינו קודם: נאמר ש-{% equation %}a<b{% endequation %} אם {% equation %}b-a\in P{% endequation %}. ונרחיב את הסימון כך ש-{% equation %}a\le b{% endequation %} אם {% equation %}a<b{% endequation %} או {% equation %}a=b{% endequation %}.

אנחנו רגילים לחשוב על {% equation %}\le{% endequation %} בתור <strong>יחס סדר</strong>, כלומר משהו שמקיים שלוש אקסיומות משל עצמו:

<ul> <li>{% equation %}a\le a{% endequation %} לכל {% equation %}a{% endequation %} ("רפלקסיביות")</li>


<li>אם {% equation %}a\le b{% endequation %} וגם {% equation %}b\le a{% endequation %} אז {% equation %}a=b{% endequation %} ("אנטיסימטריות")</li>


<li>אם {% equation %}a\le b{% endequation %} וגם {% equation %}b\le c{% endequation %} אז {% equation %}a\le c{% endequation %} ("טרנזיטיביות")</li>

</ul>

אפשר להוכיח ש-{% equation %}\le{% endequation %} שלנו מקיים את שלוש התכונות הללו.

רפלקסיביות זה פשוט על פי הגדרה: אמרנו שאם {% equation %}a=b{% endequation %} אז {% equation %}a\le b{% endequation %} אז ברור שלכל {% equation %}a{% endequation %} מתקיים {% equation %}a\le a{% endequation %}.

אנטיסימטריות זה גם כן די פשוט. אם {% equation %}a=b{% endequation %} סיימנו, אחרת נניח ש-{% equation %}a\ne b{% endequation %} ולכן ההנחות שלנו הן ש-{% equation %}a<b{% endequation %} וגם {% equation %}b<a{% endequation %}, כלומר על פי ההגדרה שלנו {% equation %}b-a\in P{% endequation %} וגם {% equation %}a-b\in P{% endequation %}. עכשיו, שימו לב ש-{% equation %}a-b=-\left(b-a\right){% endequation %} (צריך להוכיח את זה מאקסיומות השדה אבל זה קל) אז הגענו לסתירה: מצאנו איבר שגם הוא וגם הנגדי שלו שייכים שניהם ל-{% equation %}P{% endequation %}, בסתירה לאקסיומה שאומרת שבדיוק אחד משניהם שייך ל-{% equation %}P{% endequation %}. המסקנה היא שההנחה ש-{% equation %}a\ne b{% endequation %} לא הייתה נכונה ולכן {% equation %}a=b{% endequation %}, שזה מה שרצינו.

עבור הטרנזיטיביות, הנתון שלנו הוא {% equation %}a\le b{% endequation %} וגם {% equation %}b\le c{% endequation %}. אם {% equation %}a=b{% endequation %} אז מ-{% equation %}b\le c{% endequation %} ברור ש-{% equation %}a\le c{% endequation %} (פשוט כותבים {% equation %}a{% endequation %} במקום {% equation %}b{% endequation %}) ובדומה אם {% equation %}b=c{% endequation %} אז מ-{% equation %}a\le b{% endequation %} ברור ש-{% equation %}a\le c{% endequation %}. לכן נשאר לנו להוכיח רק שאם {% equation %}a<b{% endequation %} וגם {% equation %}b<c{% endequation %} אז {% equation %}a\le c{% endequation %}. משתי ההנחות הללו אנחנו מקבלים {% equation %}b-a\in P{% endequation %} וגם {% equation %}c-b\in P{% endequation %} ועל פי הסגירות של {% equation %}P{% endequation %} לחיבור נקבל ש-{% equation %}c-a=\left(c-b\right)+\left(b-a\right)\in P{% endequation %}, כמו שרצינו.

בתורת הקבוצות כשמדברים על יחסי סדר, שלוש האקסיומות למעלה מגדירות את מה שנקרא <strong>סדר חלקי</strong>. בסדר חלקי, ייתכן שיהיו איברים שבכלל אי אפשר להשוות ביניהם, וזה יכול לסבך מאוד דברים. אצלנו, ביחס הסדר של שדה סדור, זה פשוט לא יכול לקרות ויחס הסדר יהיה מה שנקרא <strong>מלא</strong>, כלומר לכל {% equation %}a,b\in\mathbb{F}{% endequation %} או שמתקיים {% equation %}a<b{% endequation %} או שמתקיים {% equation %}b<a{% endequation %} או שמתקיים {% equation %}a=b{% endequation %}. זה נובע ישירות מכך ש-{% equation %}b-a\in P{% endequation %} או ש-{% equation %}-\left(b-a\right)\in P{% endequation %} או ש-{% equation %}b-a=0{% endequation %}, כלומר מהאקסיומה הראשונה שהייתה לנו על {% equation %}P{% endequation %}.

הוכחנו כאן ש-{% equation %}\le{% endequation %} הוא יחס סדר כמו שלומדים בקורס בתורת הקבוצות, אבל למה לעצור כאן? בואו נוכיח את הטענות שראינו בבית הספר! למשל, שאם {% equation %}x<y{% endequation %} ובנוסף {% equation %}a>0{% endequation %} אז {% equation %}ax<ay{% endequation %}. כדי להוכיח את זה, נסתכל על {% equation %}ay-ax=a\left(y-x\right){% endequation %}. מכך ש-{% equation %}x<y{% endequation %} אנחנו מקבלים ש-{% equation %}y-x\in P{% endequation %} ומכך ש-{% equation %}a>0{% endequation %} אנחנו מקבלים ש-{% equation %}a\in P{% endequation %} (כי {% equation %}a=a-0\in P{% endequation %}) ולכן המכפלה שלהם גם שייכת ל-{% equation %}P{% endequation %} וקיבלנו את מה שרצינו.

עוד דבר שראינו בבית הספר הוא שכפל במספר שלילי <strong>הופך</strong> את כיוון אי השוויון, כלומר אם {% equation %}x<y{% endequation %} ו-{% equation %}a<0{% endequation %} אז {% equation %}ax>ay{% endequation %}. כדי להוכיח את זה, בואו נסתכל על {% equation %}ax-ay=a\left(x-y\right)=-a\left(y-x\right){% endequation %}. מכיוון ש-{% equation %}x<y{% endequation %} אז {% equation %}y-x\in P{% endequation %} ומכיוון ש-{% equation %}a<0{% endequation %} אז {% equation %}-a\in P{% endequation %} ולכן שוב קיבלנו מכפלה ששייכת ל-{% equation %}P{% endequation %}, כפי שרצינו.

ועוד דבר שראינו בבית הספר הוא שגם לקחת הופכי לשני האגפים של אי שוויון במספרים חיוביים <strong>הופך</strong> את כיוון אי השוויון. כלומר, אם {% equation %}0<x<y{% endequation %} אז {% equation %}x^{-1}>y^{-1}{% endequation %}. כדי לראות את זה, פשוט נכפול את שני האגפים של {% equation %}x<y{% endequation %} ב-{% equation %}x^{-1}{% endequation %} מצד שמאל ואז נכפול את שני האגפים ב-{% equation %}y^{-1}{% endequation %} מצד ימין ונקבל {% equation %}y^{-1}<x^{-1}{% endequation %}. הכל מסתדר מאוד נחמד.

עוד משהו נחמד הוא שעכשיו אנחנו יכולים להגדיר <strong>ערך מוחלט</strong>. זו פונקציה קטנה ותמימה למראה שהופכת לקריטית ממש כשמתחילים לדבר על חשבון דיפרנציאלי ואינטגרלי, וקל להגדיר אותה בכל שדה סדור (אפשר להגדיר אותה גם בשדות לא סדורים אבל זה סיפור אחר). לכל {% equation %}x{% endequation %} נגדיר

{% equation %}\left|x\right|=\begin{cases} x & x\ge0\\ -x & x<0 \end{cases}{% endequation %}

ומה שנחמד לראות הוא שכבר בהגדרה האבסטרקטית הזו, מתקיימות התכונות הבסיסיות שאנחנו רגילים אליהן מערך מוחלט "רגיל" ואפשר להוכיח אותן מהכמות הבאמת זעומה של אקסיומות שעליהן הסתמכנו.

ראשית, אם {% equation %}x\ne0{% endequation %}, אז גם {% equation %}\left|x\right|\ne0{% endequation %}, פשוט כי אם {% equation %}x\ne0{% endequation %} אז {% equation %}\left|x\right|{% endequation %} הוא או {% equation %}x{% endequation %} או {% equation %}-x{% endequation %} ושניהם שונים מאפס.

שנית, לכל {% equation %}x,y\in\mathbb{F}{% endequation %} מתקיים {% equation %}\left|xy\right|=\left|x\right|\cdot\left|y\right|{% endequation %}, כלומר פונקציית הערך המוחלט היא <strong>כפלית</strong>. את זה אפשר לראות למשל על ידי בדיקה מפורשת של כל: למשל, אם {% equation %}x,y\ge0{% endequation %} אז {% equation %}\left|x\right|=x,\left|y\right|=y{% endequation %} וכמו כן {% equation %}xy\ge0{% endequation %} ולכן {% equation %}\left|xy\right|=xy=\left|x\right|\left|y\right|{% endequation %}. והנה דוגמא טיפה יותר מסובכת: אם {% equation %}x\ge0{% endequation %} אבל {% equation %}y<0{% endequation %} אז {% equation %}xy\le0{% endequation %} ולכן נצטרך לחלק פה למקרים: אם {% equation %}x=0{% endequation %} אז {% equation %}xy=0=0\cdot\left|y\right|=\left|x\right|\cdot\left|y\right|{% endequation %} . לעומת זאת אם {% equation %}x>0{% endequation %} אז {% equation %}xy<0{% endequation %} ולכן {% equation %}\left|xy\right|=-xy=x\left(-y\right)=\left|x\right|\left|y\right|{% endequation %}, וכן הלאה.

התכונה השלישית היא המעניינת מכולן: <strong>אי-שוויון המשולש</strong>, שאפילו שמו מגיע לו מגאומטריה שפשוט לא קיימת כאן, בעולם של ההגדרות האלגבריות הטהורות:

{% equation %}\left|x+y\right|\le\left|x\right|+\left|y\right|{% endequation %}

הטריק בהוכחה הוא לשים לב שלכל {% equation %}a\in\mathbb{F}{% endequation %} מתקיים {% equation %}\left|a\right|^{2}=a^{2}{% endequation %} פשוט כי אם {% equation %}a\ge0{% endequation %} זה ברור ואם {% equation %}a<0{% endequation %} אז {% equation %}\left|a\right|^{2}=\left(-a\right)\left(-a\right)=a^{2}{% endequation %} כי מינוס כפול מינוס זה פלוס, כמו שראינו. אז אפשר לכתוב:

{% equation %}\left|x+y\right|^{2}=\left(x+y\right)^{2}=x^{2}+2xy+y^{2}\le{% endequation %}

{% equation %}\left|x\right|^{2}+2\left|xy\right|+\left|y\right|^{2}=\left|x\right|^{2}+2\left|x\right|\left|y\right|+\left|y\right|^{2}=\left(\left|x\right|+\left|y\right|\right)^{2}{% endequation %}

כאן השתמשנו בכך ש-{% equation %}xy\le\left|xy\right|{% endequation %}, שקל להוכיח באופן כללי כי אם {% equation %}a\ge0{% endequation %} אז {% equation %}a=\left|a\right|{% endequation %} ואם {% equation %}a<0{% endequation %} אז {% equation %}-a>0{% endequation %} ואז {% equation %}-a-a=-2a>0{% endequation %} כך ש-{% equation %}a<-a=\left|a\right|{% endequation %}.

הגענו אל המסקנה {% equation %}\left|x+y\right|^{2}\le\left(\left|x\right|+\left|y\right|\right)^{2}{% endequation %}. מה שאנחנו באמת רוצים לעשות הוא "להוציא שורש" משני האגפים. כלומר, להראות שאם {% equation %}a,b\ge0{% endequation %} שניהם וגם {% equation %}a^{2}\le b^{2}{% endequation %} אז {% equation %}a\le b{% endequation %}. הנה דרך אחת להראות את זה: אם {% equation %}a^{2}\le b^{2}{% endequation %} אז {% equation %}b^{2}-a^{2}\ge0{% endequation %} אבל {% equation %}b^{2}-a^{2}=\left(b-a\right)\left(b+a\right){% endequation %}. עכשיו, הנחנו ש-{% equation %}a,b\ge0{% endequation %} ולכן {% equation %}b+a\ge0{% endequation %}. מכאן שאם לא היה מתקיים {% equation %}a\le b{% endequation %} אז היה מתקיים {% equation %}b-a<0{% endequation %} מה שהיה גורר ש-{% equation %}b^{2}-a^{2}<0{% endequation %}, בסתירה להנחה המקורית שלנו. זה מסיים את ההוכחה של אי שוויון המשולש.

<h3>ארכימדיות</h3>

אני רוצה לתת עכשיו עוד הגדרה די מהותית, שתהפוך להיות חשובה מאוד בהמשך: <strong>ארכימדיות</strong> של שדה סדור (מארכימדס, המתמטיקאי היווני). דרך אחת לנסח את תכונת הארכימדיות של שדה סדור {% equation %}\mathbb{F}{% endequation %} היא שלכל {% equation %}a\in\mathbb{F}{% endequation %} קיים {% equation %}n\in\mathbb{Z}{% endequation %} כך ש-{% equation %}a<n{% endequation %} . כאן צריך לחדד שב-{% equation %}\mathbb{Z}{% endequation %} הכוונה שלי היא לתת-הקבוצה של {% equation %}\mathbb{F}{% endequation %} שנוצרת על ידי חיבור/חיסור של {% equation %}1{% endequation %} לעצמו (זכרו שמקבלים את {% equation %}\mathbb{Z}{% endequation %} רק אם השדה ממציין 0, אבל אם הוא לא ממציין 0 הוא בפרט לא סדור). במילים אחרות, האיברים של השדה אף פעם לא "בורחים" מבחינת גודלם למספרים הטבעיים.

יש עוד כמה דרכים לראות את זה. ראשית, ארכימדיות הוגדרה בתור "קיים {% equation %}n{% endequation %} גדול יותר" אבל מזה נובע מייד גם "קיים {% equation %}n{% endequation %} קטן יותר", כלומר לכל {% equation %}a\in\mathbb{F}{% endequation %} קיים {% equation %}n\in\mathbb{Z}{% endequation %} כך ש-{% equation %}n<a{% endequation %}. כדי לראות את זה, פשוט נפעיל ארכימדיות "רגילה" על {% equation %}-a{% endequation %}, נקבל שקיים {% equation %}n^{\prime}{% endequation %} כך ש-{% equation %}-a<n^{\prime}{% endequation %}, נכפול את שני האגפים ב-{% equation %}-1{% endequation %}, מה שכבר ראינו שהופך את הסדר, נסמן {% equation %}n=-n^{\prime}{% endequation %} ונקבל {% equation %}n<a{% endequation %}.

שנית, "קיים מספר טבעי גדול כרצוננו" זה אותו הדבר כמו "קיים מספר רציונלי חיובי קטן כרצוננו". כלומר, לכל {% equation %}a>0{% endequation %} קיים {% equation %}n\in\mathbb{Z}{% endequation %} כך ש-{% equation %}\frac{1}{n}<a{% endequation %} - כדי לראות את זה, ניקח {% equation %}n{% endequation %} כך ש-{% equation %}a^{-1}<n{% endequation %} ואז ניקח הופכי לשני האגפים ונקבל {% equation %}\frac{1}{n}<a{% endequation %}.

עוד דרך לחשוב על זה, שאני אוהב במיוחד, היא זו: בואו ניקח {% equation %}\varepsilon>0{% endequation %} כלשהו, כשהאינטואיציה היא לחשוב על {% equation %}\varepsilon{% endequation %} בתור משהו ממש ממש קטן (זה השימוש הסטנדרטי של האות הזו בחדו"א). בואו ניקח גם {% equation %}M>0{% endequation %} כלשהו, כשהאינטואיציה היא לחשוב עליו בתור מספר ממש ממש ענק. אז ארכימדיות פירושה שקיים {% equation %}n{% endequation %} כך ש-{% equation %}n>\frac{M}{\varepsilon}{% endequation %}, או במילים אחרות {% equation %}n\varepsilon>M{% endequation %}. זה אומר שלא משנה עד כמה משהו קטן - אם אנחנו בשדה ארכימדי, לחבר אותו מספר פעמים לעצמו יגרום לו לעבור בגודלו כל מספר כולל ענקיים.

כמובן, שאלה מתבקשת עכשיו היא אילו שדות סדורים הם לא ארכימדיים. התשובה היא שיש כאלו, אבל להציג אותם קונקרטית יהיה מתוסבך מדי אם אני רוצה לסיים מהר את החלק הזה. עדיין, בואו נחשוב מה המשמעות של קיום שלהם. יש למשל שדה לא ארכימדי שמרחיב את הממשיים, {% equation %}\mathbb{R}{% endequation %} (שדה ה"היפר-ממשיים"). בשדה כזה יהיה איבר {% equation %}\omega{% endequation %} כך ש-{% equation %}n<\omega{% endequation %} לכל {% equation %}n{% endequation %} טבעי; על {% equation %}\omega{% endequation %} הזה אפשר לחשוב בתור איבר מגודל "אינסופי". מכיוון שאנחנו בשדה קיים לו הופכי, {% equation %}\omega^{-1}{% endequation %}; אי השוויון {% equation %}n<\omega{% endequation %} מלמד אותנו ש-{% equation %}\omega^{-1}<\frac{1}{n}{% endequation %}. כלומר נקבל ש-{% equation %}\omega^{-1}{% endequation %} קטן מכל מספר ממשי (כי לכל מספר ממשי קיים {% equation %}\frac{1}{n}{% endequation %} שקטן ממנו); {% equation %}\omega^{-1}{% endequation %} הוא מה שמכונה במתמטיקה מודרנית "אינפיניטסימל" (מושג שהייתה לו משמעות הרבה יותר רופפת בימי התהוות החדו"א).

הקיום של שדות לא ארכימדיים שמכלילים את הממשיים הוא מבחינתי תמרור אזהרה עצום להגדרה של הממשיים בתור "כל המספרים על ציר המספרים". הגישה הזו מניחה שהאינפיניטסימל {% equation %}\omega^{-1}{% endequation %} בכלל לא נמצא על ציר המספרים. עוד הייתי יכול להבין טענות ש-{% equation %}\omega{% endequation %} לא נמצא עליו כי הוא אי שם הרחק באינסוף רחוק רחוק - אבל לטעון ש-{% equation %}\omega^{-1}{% endequation %} הוא לא על ציר המספרים, בהינתן כמה שהוא קרוב לאפס - זה כבר מוזר. אני אישית לא מצליח לחשוב על דרך טובה לנמק למה אסור למה שאנחנו קוראים לו "ציר המספרים" לכלול את {% equation %}\omega^{-1}{% endequation %} בלי פשוט לומר "אנחנו מגדירים את ציר המספרים להיות {% equation %}\mathbb{R}{% endequation %}" וחסל (זו הגישה שלי), מה שכמובן מונע מאיתנו להגדיר את {% equation %}\mathbb{R}{% endequation %} בתור ציר המספרים.

<h3>צפיפות</h3>

לפני שנמשיך לחלק הבא, יש עוד תכונה סופר-חשובה אחת שתהיה סופר-שימושית בהמשך שכבר אפשר לדבר עליה. מה ההבדל העקרוני בין {% equation %}\mathbb{Z}{% endequation %} ובין {% equation %}\mathbb{Q}{% endequation %} בתור חוגים סדורים? ובכן, {% equation %}\mathbb{Q}{% endequation %} הוא לא סתם חוג אלא שדה וזה באמת הבדל מהותי, אבל אני חושב יותר על הבדל שקשור ליחס הסדר עצמו. ב-{% equation %}\mathbb{Z}{% endequation %}, מתקיים למשל אי השוויון {% equation %}3<4{% endequation %}, ויוצא שבין שני המספרים הללו אין עוד איבר נוסף - אני יכול "לדלג בצעד אחד" מ-{% equation %}3{% endequation %} אל {% equation %}4{% endequation %}. לעומת זאת ב-{% equation %}\mathbb{Q}{% endequation %} אין דבר כזה: לכל {% equation %}a,b\in\mathbb{Q}{% endequation %} כך ש-{% equation %}a<b{% endequation %} קיים {% equation %}c\in\mathbb{Q}{% endequation %} כך ש-{% equation %}a<c<b{% endequation %}. התכונה הזו, של קיום איבר <strong>בין</strong> כל זוג איברים שונים זה מזה נקרא <strong>צפיפות</strong> ובאמת שהוא חשוב בצורה בלתי רגילה. אז ההבדל בין {% equation %}\mathbb{Z}{% endequation %} ובין {% equation %}\mathbb{Q}{% endequation %} שרציתי לדבר עליו: יחס הסדר של {% equation %}\mathbb{Z}{% endequation %} לא צפוף אבל של {% equation %}\mathbb{Q}{% endequation %} כן.

המקרה של {% equation %}\mathbb{Z}{% endequation %} מראה לנו שקיימים חוגים סדורים שאינם צפופים. אבל האם כל <strong>שדה</strong> סדור הוא צפוף? ובכן, כן, בצורה לא מעניינת: יהיו {% equation %}a<b{% endequation %} איברים כלשהם של שדה סדור {% equation %}\mathbb{F}{% endequation %}, אז {% equation %}a=\frac{a+a}{2}<\frac{a+b}{2}<\frac{b+b}{2}=b{% endequation %} ולכן {% equation %}\frac{a+b}{2}{% endequation %} הוא איבר שנמצא בין {% equation %}a{% endequation %} לבין {% equation %}b{% endequation %}. בגלל שזה היה פשוט <strong>מדי</strong>, אנחנו יכולים לחפש תכונת צפיפות <strong>עוד יותר</strong> יעילה. מה שהוכחתי הוא שבכל שדה סדור {% equation %}\mathbb{F}{% endequation %}, לכל זוג איברים {% equation %}a,b\in\mathbb{F}{% endequation %} קיים {% equation %}c\in\mathbb{F}{% endequation %} כך ש-{% equation %}a<c<b{% endequation %}. עכשיו, בגלל ש-{% equation %}\mathbb{F}{% endequation %} שדה <strong>סדור</strong> הוא ממציין 0 ולכן מכיל עותק של {% equation %}\mathbb{Q}{% endequation %}, ואני יכול להראות שהעותק הזה של {% equation %}\mathbb{Q}{% endequation %} צפוף <strong>בתוך</strong> {% equation %}\mathbb{F}{% endequation %} במובן הזה שאת ה-{% equation %}c{% endequation %} שנמצא בין כל {% equation %}a,b\in\mathbb{F}{% endequation %} אני יכול לבחור מתוך {% equation %}\mathbb{Q}{% endequation %}. למה ההוכחה הנוכחית לא עובדת? כי אני בונה את {% equation %}c{% endequation %} שלי בתור הסכום {% equation %}\frac{a+b}{2}{% endequation %}, מה שנותן לי משהו שאנחנו רק יודעים עליו שהוא איבר כללי ב-{% equation %}\mathbb{F}{% endequation %} ולכן לא חייב להיות רציונלי. ובאמת, עבור {% equation %}\mathbb{F}{% endequation %} <strong>לא ארכימדי</strong> אני לא אוכל לקבל צפיפות של {% equation %}\mathbb{Q}{% endequation %} בתוך {% equation %}\mathbb{F}{% endequation %}. אבל אם {% equation %}\mathbb{F}{% endequation %} ארכימדי, אפשר להוכיח את זה.

הנקודה המרכזית היא שאם {% equation %}b-a>1{% endequation %}, אז <strong>קל</strong> למצוא איבר רציונלי ביניהם, ולא סתם רציונלי אלא ממש מספר שלם. למה? ובכן, התכונה הארכימדית אומרת לנו שקיים {% equation %}m{% endequation %} שלם כך ש-{% equation %}a<m{% endequation %}. יש הרבה {% equation %}m{% endequation %}-ים כאלו, אבל אני יכול לבחור מתוכם את <strong>המינימלי</strong>. זה דורש נימוק בפני עצמו, אבל הנה נימוק זריז: ראשית, מכיוון שהשדה ארכימדי קיים {% equation %}n_{1}{% endequation %} כך ש-{% equation %}n_{1}<a{% endequation %} וגם קיים {% equation %}n_{2}{% endequation %} כך ש-{% equation %}a<n_{2}{% endequation %}. עכשיו אפשר להסתכל על הקבוצה {% equation %}\left\{ n\in\mathbb{Z}\ |n_{1}\le n\le n_{2},a<n\right\} {% endequation %}. זו קבוצה <strong>סופית</strong> כי יש רק מספר סופי של שלמים בין {% equation %}n_{1}{% endequation %} ל-{% equation %}n_{2}{% endequation %} - בדיוק {% equation %}n_{2}-n_{1}+1{% endequation %} כאלו. כמו כן זו לא קבוצה ריקה, כי לפחות עבור {% equation %}n_{2}{% endequation %} אנחנו יודעים ש-{% equation %}a<n_{2}{% endequation %}. לכן קיים לה איבר מינימלי {% equation %}m{% endequation %} (אני עוד מעט אדבר על איברים מינימליים יותר בפירוט, למי שעדיין חשדנים). ה-{% equation %}m{% endequation %} הזה יקיים ש-{% equation %}a<m{% endequation %} אבל {% equation %}m-1<a{% endequation %}.

עכשיו, נתון לי ש-{% equation %}b-a>1{% endequation %}, כלומר {% equation %}a+1<b{% endequation %}. ניקח את {% equation %}m-1<a{% endequation %}, נחבר 1 לשני האגפים, ונקבל {% equation %}m<a+1<b{% endequation %}; קיבלנו ש-{% equation %}a<m<b{% endequation %}, כמו שרצינו.

זה מסיים את הוכחת הצפיפות למקרה של {% equation %}b-a>1{% endequation %}. באופן כללי, אם {% equation %}a<b{% endequation %} אז {% equation %}b-a>0{% endequation %} ולכן ארכימדיות נותנת לנו שקיים {% equation %}n>0{% endequation %} שלם כך ש-{% equation %}\frac{1}{b-a}<n{% endequation %}. נכפול את שני האגפים ב-{% equation %}b-a{% endequation %} ונקבל {% equation %}1<bn-an{% endequation %}, ועכשיו אני יכול להשתמש במה שהוכחתי לפני רגע ולהראות שקיים {% equation %}m{% endequation %} שלם כך ש-{% equation %}an<m<bn{% endequation %}. לסיום אני אחלק את כל האגפים ב-{% equation %}n{% endequation %} ואקבל {% equation %}a<\frac{m}{n}<b{% endequation %}, וסיימנו! זה לא היה קל במיוחד אבל זו תוצאה שימושית ביותר.

<h2>שלם</h2>

<h3>מה בעצם חסר?</h3>

בשלב הזה אנחנו יודעים מה זה שדה סדור, וגם יש לנו דוגמא טובה לשדה סדור שכזה: {% equation %}\mathbb{Q}{% endequation %}. אז מה עוד אנחנו צריכים?

ובכן, ראשית אנחנו צריכים <strong>מספרים</strong>. חסרים לנו מספרים. לא יעלה על הדעת שנסתפק במספרים שיש ב-{% equation %}\mathbb{Q}{% endequation %}. אם אני מצייר ריבוע עם אורך צלע 1 ומותח בו אלכסון, האורך של האלכסון הזה יהיה {% equation %}\sqrt{2}{% endequation %} (נובע ממשפט פיתגורס). אבל {% equation %}\sqrt{2}\notin\mathbb{Q}{% endequation %}, אז חסרים לי מספרים. אני רוצה לפחות את כל השורשים {% equation %}\sqrt{n}{% endequation %} לכל {% equation %}n\ge0{% endequation %}. ולמה לא גם את השורשים השלישיים, {% equation %}\sqrt[3]{n}{% endequation %}? ובעצם שיהיה {% equation %}\sqrt[k]{n}{% endequation %} לכל {% equation %}n\ge0{% endequation %} ו-{% equation %}k>0{% endequation %}. אפשר אפילו להגדיל ולומר שאני רוצה את כל המספרים <strong>האלגבריים</strong>, כלומר כל המספרים שאני יכול לקבל בתור שורשים של פולינום עם מקדמים רציונליים, אבל אני מעדיף לא ללכת לכיוון של טענות כאלו כי הן שוב מניחות שאני כבר מכיר את "העולם הרחב" של המספרים ופשוט גוזר מתוכו תת-קבוצה מעניינת, וכרגע אני רק רוצה להצביע על מספרים קונקרטיים שברור שחסרים לי. גם {% equation %}\pi{% endequation %} חסר. גם {% equation %}e{% endequation %} חסר. בקיצור, {% equation %}\mathbb{Q}{% endequation %} ממש לא מספיק.

העניין הוא שאם אני אוסיף את כל המספרים הללו, הכל הולך ממש להסתבך. ראיתי למשל שאם אני מוסיף את {% equation %}\sqrt{2}{% endequation %} ל-{% equation %}\mathbb{Q}{% endequation %} ו"סוגר" את הקבוצה כך שעדיין אקבל שדה, אני אצטרך להוסיף את כל האיברים מהצורה {% equation %}a+b\sqrt{2}{% endequation %} כך ש-{% equation %}a,b\in\mathbb{Q}{% endequation %}. אם אני אוסיף את {% equation %}\pi{% endequation %} זה יהיה יותר בעייתי - אני אצטרך להוסיף את כל האיברים מהצורה {% equation %}a_{0}+a_{1}\pi+a_{2}\pi^{2}+a_{3}\pi^{3}+\ldots+a_{k}\pi^{k}{% endequation %}. אבל אפילו זה לא מספיק, כי מכיוון ש-{% equation %}\pi>1{% endequation %} אז {% equation %}0<\pi^{-1}<1{% endequation %} ולכן אני יכול לקחת סכומים <strong>אינסופיים</strong> של חזקות שליליות של {% equation %}\pi{% endequation %} ולצפות שזה יתכנס למשהו, ובעצם אני מכניס לתמונה המון שיקולים של חדו"א למרות <strong>שעדיין לא פיתחתי את החדו"א כי אין לי איפה</strong> כי החדו"א הרי מתחיל מזה שמדברים על השדה שבו האקשן הולך להתרחש. בקיצור, כל הגישה הזו של "בואו נרחיב את {% equation %}\mathbb{Q}{% endequation %} עם איברים קונקרטיים" היא קצת מבורחשת, ואני לא רוצה לנקוט בה בכלל (וגם הבניות הקונקרטיות של {% equation %}\mathbb{R}{% endequation %} שאראה בהמשך לא עושות את זה).

מה שאני אעשה, כמו קודם, הוא לשאול את עצמי - איזו אקסיומה חסרה לי? איזו תכונה נוספת של השדה הסדור שאני בונה תיתן לי את מה שאני צריך? וכאן מגיעות בשורות טובות נחמדות מאוד: יש אקסיומה <strong>אחת</strong>, פשוטה יחסית לניסוח מילולי ודי אינטואיטיבית מבחינת מה שהיא עושה, שהיא <strong>כל</strong> מה שחסר לי. מרגע שאוסיף אותה אקבל את {% equation %}\sqrt{2}{% endequation %} ואת {% equation %}\pi{% endequation %} ואת {% equation %}e{% endequation %} ואת כל המספרים שחסרים לי, והשדה שאני בונה יהפוך להיות מקום <strong>ממש נחמד</strong> שבו אפשר להוכיח את כל משפטי הבסיס של החדו"א (שלא אציג בפוסט הזה אבל נראה בהמשך למה הם צריכים דווקא את האקסיומה הזו). האקסיומה המושלמת הזו נקראת <strong>אקסיומת השלמות</strong> (באנגלית משחק המילים הדלוח הזה לא עובד; היא נקראת Axiom of Completeness). הנה הניסוח שלה, ותכף אסביר מה הוא אומר: <strong>לכל קבוצה לא ריקה וחסומה מלעיל קיים חסם עליון</strong>.

מה זו קבוצה אנחנו יודעים. בהקשר שלנו יש לנו שדה {% equation %}\mathbb{F}{% endequation %} ו"קבוצה" היא בסך הכל אוסף של איברים מתוכו, מה שמסומן ב-{% equation %}A\subseteq\mathbb{F}{% endequation %}. הקבוצה הריקה מסומנת ב-{% equation %}\emptyset{% endequation %} אז כדי להגיד שקבוצה לא ריקה אנחנו כותבים {% equation %}A\ne\emptyset{% endequation %}. החלק הבאמת מעניין בהגדרה הוא זה שמערב את המילה "חסם" להטיותיה השונות.

<h3>חסמים</h3>

קבוצה <strong>חסומה</strong> זה כבר עניין של הכנסת יחס הסדר {% equation %}\le{% endequation %} לתמונה. אנחנו אומרים ש-{% equation %}A{% endequation %} <strong>חסומה מלעיל</strong> ("חסומה מלמעלה") אם קיים {% equation %}b\in\mathbb{F}{% endequation %} כך שלכל {% equation %}a\in A{% endequation %} מתקיים {% equation %}a\le b{% endequation %}. יש כמובן גם הגדרה מקבילה עבור חסם מלמטה: אומרים ש-{% equation %}A{% endequation %} <strong>חסומה מלרע</strong> אם קיים {% equation %}b\in\mathbb{F}{% endequation %} כך שלכל {% equation %}a\in A{% endequation %} מתקיים {% equation %}b\le a{% endequation %}, ואנחנו אומרים ש-{% equation %}A{% endequation %} <strong>חסומה</strong> אם היא חסומה גם מלעיל וגם מלרע (למרות שבטח לפעמים יתפקשש לי סתם "חסומה" גם על קבוצה שחסומה רק מכיוון אחד). הנה כמה דוגמאות פשוטות עבור המקרה של {% equation %}\mathbb{F}=\mathbb{Q}{% endequation %}: הקבוצה {% equation %}A=\mathbb{N}{% endequation %} היא חסומה מלרע (על ידי 0, למשל) אבל לא חסומה מלעיל. לעומת זאת הקבוצה {% equation %}\left\{ \frac{1}{n}\ |\ n\in\mathbb{N}^{+}\right\} {% endequation %} ({% equation %}\mathbb{N}^{+}{% endequation %} פירושו הטבעיים פרט ל-0, ולא משנה אם בהגדרה שלנו הטבעיים כוללים את 0 או לא) חסומה גם מלרע (על ידי 0 שוב) וגם מלעיל (על ידי 1). שימו לב להבדל בין שני החסמים: בעוד ש-1 הוא איבר של הקבוצה ({% equation %}1=\frac{1}{1}{% endequation %}), 0 הוא לא איבר של הקבוצה. על 1 אנחנו אומרים שהוא גם <strong>איבר מקסימלי</strong> של הקבוצה, אבל מה נגיד על 0? ובכן, נגיד שהוא <strong>חסם תחתון</strong>, אבל אני מקדים את המאוחר.

ראשית בואו נדבר על מינימום ומקסימום. אם {% equation %}A{% endequation %} קבוצה, וקיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}b\le a{% endequation %} לכל {% equation %}b\in A{% endequation %} אז אומרים ש-{% equation %}a{% endequation %} הוא <strong>המקסימום</strong> של {% equation %}A{% endequation %} ומסמנים {% equation %}a=\max A{% endequation %}. באופן דומה, אם קיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}a\le b{% endequation %} לכל {% equation %}b\in A{% endequation %} אז אומרים ש-{% equation %}a{% endequation %} הוא <strong>המינימום</strong> של {% equation %}A{% endequation %} ומסמנים {% equation %}a=\min A{% endequation %}. לקבוצה יכול להיות רק מקסימום יחיד, כי אם {% equation %}a,a^{\prime}{% endequation %} שניהם מקיימים את ההגדרה אז בגלל ששניהם איברים בקבוצה, מתקיים גם {% equation %}a\le a^{\prime}{% endequation %} וגם {% equation %}a^{\prime}\le a{% endequation %} ומאנטיסימטריות נובע ש-{% equation %}a=a^{\prime}{% endequation %}, ובאופן דומה גם המינימום הוא יחיד, אם הוא קיים. אבל הוא לא חייב להיות קיים, ובואו נראה מה יכול להשתבש.

ראשית, אם {% equation %}A=\emptyset{% endequation %} אז לא יכול להיות בה מקסימום מהטעם הפשוט שמקסימום חייב להיות איבר בקבוצה וזה קצת קשה עבור קבוצה בלי איברים. שנית, אם {% equation %}A{% endequation %} לא חסומה מלעיל אז מן הסתם לא יהיה לה מקסימום, כי אם אין <strong>בכלל</strong> מישהו שגדול או שווה לכל אברי הקבוצה, ברור שלא יהיה מישהו שהוא <strong>גם</strong> בקבוצה וגם גדול או שווה לכל איבריה. אבל גם בלי שתי הבעיות הברורות האלו, עדיין יכולות להיות קבוצות שהן לא ריקות, חסומות מלעיל ואין להן מקסימום. הנה דוגמא - הקבוצה

{% equation %}\left\{ 0.9,0.99,0.999,\ldots\right\} {% endequation %}

אפשר לחשוב על האיברים בקבוצה הזו כאילו הם עולים ועולים, {% equation %}0.9<0.99<0.999<\ldots{% endequation %}, אבל הם אף פעם לא עוברים את 1. מצד שני, הם גם לא מגיעים אל 1, כי כל איבר בקבוצה הזו הוא מהצורה {% equation %}1-\frac{1}{10^{n}}{% endequation %} עבור {% equation %}n\ge1{% endequation %}, ולכן תמיד קטן מ-1. <strong>אם</strong> הייתי מוסיף את 1 לקבוצה, אז הוא היה האיבר המקסימלי שלה; אבל הוא לא שם. 

שימו לב שהסיטואציה הזו דרשה ממני קבוצה עם אינסוף איברים. אם יש קבוצה לא ריקה עם מספר <strong>סופי</strong> של איברים, תמיד קיים לה מקסימום. הנה הוכחה פשוטה: לקבוצה בת איבר אחד יש מקסימום - האיבר האחד הזה. נניח באינדוקציה שלקבוצה בת {% equation %}n{% endequation %} איברים יש תמיד מקסימום; תהא {% equation %}A=\left\{ a_{1},\ldots,a_{n},a_{n+1}\right\} {% endequation %} קבוצה עם {% equation %}n+1{% endequation %} איברים. אז לקבוצה {% equation %}A^{\prime}=\left\{ a_{1},\ldots,a_{n}\right\} {% endequation %} יש מקסימום, {% equation %}b=\max A^{\prime}{% endequation %}. עכשיו, אם {% equation %}a_{n+1}>b{% endequation %} אז קל לראות ש-{% equation %}\max A=a_{n+1}{% endequation %} ואחרת קל לראות ש-{% equation %}\max A=b{% endequation %}. זה מוכיח פורמלית את הטיעון שהשתמשתי בו קודם, כשהוכחתי ש-{% equation %}\mathbb{Q}{% endequation %} היא קבוצה צפופה ב-{% equation %}\mathbb{F}{% endequation %}.

עכשיו אפשר סוף סוף לסיים את הגדרת אקסיומת השלמות. כזכור, היא אומרת "לכל קבוצה לא ריקה וחסומה מלעיל קיים חסם עליון" אז רק נשאר להסביר מה זה <strong>חסם עליון</strong>, וזה קל: זה החסם מלעיל המינימלי של הקבוצה <strong>אם הוא קיים</strong>. באופן דומה מגדירים <strong>חסם תחתון</strong> בתור החסם מלרע המקסימלי, אם הוא קיים. לשני אלו יש שמות שאני מחבב קצת יותר מאשר "חסם עליון" (שלטעמי הוא תרגום לא טוב של least upper bound כי החלק של ה-least התפספס) - <strong>סופרמום</strong> לחסם עליון ו<strong>אינפימום</strong> לחסם תחתון. והם מוגדרים פורמלית כך:

{% equation %}\sup A=\min\left\{ b\in\mathbb{F}\ |\ \forall a\in A:a\le b\right\} {% endequation %}

{% equation %}\inf A=\max\left\{ b\in\mathbb{F}\ |\ \forall a\in A:b\le a\right\} {% endequation %}

בואו נדבר על ההגדרה של סופרמום (הדיון על אינפימום יהיה זהה, אבל מעצבן להתייחס לשניהם בבת אחת). ההגדרה של סופרמום דורשת לקחת מינימום על קבוצת כל החסמים העליונים של {% equation %}A{% endequation %}. ראינו כבר שלקיחת מינימום היא פעולה "מסוכנת" כי הוא עשוי לא להיות קיים, וראינו שלוש בעיות אפשריות: ראשית, אם הקבוצה שעליה לוקחים מינימום היא ריקה - במקרה שלנו זה אומר שאין ל-{% equation %}A{% endequation %} חסמים מלעיל, כלומר שהיא לא חסומה. אז אוקיי, {% equation %}\sup A{% endequation %} לא מוגדר אם {% equation %}A{% endequation %} לא חסומה מלעיל, נשמע הגיוני.

הבעיה השניה היא אם הקבוצה שעליה לוקחים מינימום היא לא חסומה מלרע. זה אומר שלכל {% equation %}b{% endequation %}, לא משנה כמה קטן, עדיין תתקיים התכונה שלכל {% equation %}a\in A{% endequation %} מתקיים {% equation %}a\le b{% endequation %}. זה לא ממש הגיוני, כי אם ניקח {% equation %}b=a-1{% endequation %} עבור {% equation %}a\in A{% endequation %} <strong>כלשהו</strong> נקבל מישהו שהוא כבר לא חסם מלעיל של כל {% equation %}A{% endequation %}. כלומר, סיטואציה כזו יכולה לצוץ רק אם {% equation %}A{% endequation %} ריקה. כש-{% equation %}A{% endequation %} ריקה, התנאי "לכל {% equation %}a\in A{% endequation %} מתקיים {% equation %}a\le b{% endequation %}" מתקיים <strong>תמיד</strong>, לכל {% equation %}b{% endequation %}; זה מה שנקרא במתמטיקה "נכון באופן ריק" (כדי לראות למה זה ככה, שווה לחשוב על הטענה השקולה לוגית: "לא קיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}b<a{% endequation %}"; ברור שאם {% equation %}A{% endequation %} ריקה אז באמת לא קיים כזה). אז אוקיי, {% equation %}\sup A{% endequation %} לא מוגדר אם {% equation %}A{% endequation %} ריקה, נשמע הגיוני.

מה שאקסיומת השלמות אומרת הוא שאלו שתי הבעיות <strong>היחידות</strong> שיכולות להיווצר, ושבכל מקרה אחר, יהיה ל-{% equation %}A{% endequation %} סופרמום. כדי להבין למה זה כל כך חזק, ואיך זה פותר לנו בעיות ו"יוצר" לנו מספרים כמו {% equation %}\sqrt{2}{% endequation %}, בואו נראה את הדוגמא הקלאסית - הקבוצה {% equation %}A=\left\{ q\in\mathbb{Q}\ |\ q^{2}\le2\right\} {% endequation %}.

האם הקבוצה הזו לא ריקה? בוודאי, {% equation %}0\in A{% endequation %}. האם הקבוצה הזו חסומה מלעיל? בוודאי, {% equation %}2\in A{% endequation %} כי אם {% equation %}q>2{% endequation %} אז {% equation %}q^{2}>4{% endequation %} ומן הסתם לא מתקיים {% equation %}q^{2}<2{% endequation %}. מכאן שקיים לקבוצה הזו סופרמום. מי הוא יהיה? ובכן, אם ניקח את אברי {% equation %}q{% endequation %} ונגדיל אותם עוד ועוד עד שיהיה שוויון, {% equation %}q^{2}=2{% endequation %}, אז נקבל {% equation %}q=\sqrt{2}{% endequation %} ולכן האינטואיציה היא ש-{% equation %}\sup A=\sqrt{2}{% endequation %}, אבל צריך להיזהר מאוד כאן: {% equation %}\sqrt{2}{% endequation %} הוא לא מספר רציונלי, ולכן הוא לא איבר של {% equation %}A{% endequation %}, אז עדיין צריך לשלול את האפשרות שיש חסם מלעיל <strong>קטן יותר</strong> ל-{% equation %}A{% endequation %}. למרבה השמחה, קל לשלול את זה. ניקח {% equation %}r{% endequation %} כלשהו כך ש-{% equation %}r<\sqrt{2}{% endequation %}. עכשיו אפשר להשתמש בתכונת <strong>הצפיפות</strong> של הרציונליים שהוכחתי קודם ולקבל שקיים {% equation %}q\in\mathbb{Q}{% endequation %} כך ש-{% equation %}r<q<\sqrt{2}{% endequation %}. בפרט {% equation %}q^{2}<2{% endequation %} ולכן {% equation %}q\in A{% endequation %}, ולכן {% equation %}r{% endequation %} לא יכול להיות חסם מלעיל של {% equation %}A{% endequation %}, וזה <strong>לכל</strong> {% equation %}r<\sqrt{2}{% endequation %}. בנוסף, ברור ש-{% equation %}\sqrt{2}{% endequation %} עצמו הוא חסם מלעיל שכזה, כי אם {% equation %}q>\sqrt{2}{% endequation %} אז {% equation %}q^{2}>2{% endequation %} ולכן {% equation %}q\notin A{% endequation %}. זה מוכיח ש-{% equation %}\sup A=\sqrt{2}{% endequation %}.

<h3>דוגמא בעזרת שורש 2</h3>

עכשיו אני רוצה לסבך עוד יותר את העניינים, ואלו שאין להם כוח לנקודה העדינה שאני מתעקש עליה כאן מוזמנים לדלג. ההוכחה שהראיתי עכשיו חייתה "בתוך" {% equation %}\mathbb{R}{% endequation %}. היא הניחה ש-{% equation %}\sqrt{2}{% endequation %} קיים ואפשר להשתמש בצפיפות הרציונליים יחד איתו. אבל בואו נניח עכשיו שאנחנו עוברים לחיות ביקום {% equation %}\mathbb{Q}{% endequation %} ולא יודעים על שום דבר מחוצה לו, ובפרט {% equation %}\sqrt{2}{% endequation %} לא קיים מבחינתנו. האם יש דרך להוכיח שלקבוצה {% equation %}A{% endequation %} במקרה הזה פשוט <strong>לא יהיה סופרמום</strong>? אחרת {% equation %}A{% endequation %} היא לא דוגמא מעניינת כל כך - היא לא מראה לנו בעיה שיש ב"סתם" שדה סדור ושדה סדור <strong>שלם</strong> פותר.

אז בואו נוכיח שאין ל-{% equation %}A{% endequation %} סופרמום ב-{% equation %}\mathbb{Q}{% endequation %}, עם הוכחה שמשתמשת רק ב-{% equation %}\mathbb{Q}{% endequation %}. ראשית, בואו ניקח {% equation %}0<r\in\mathbb{Q}{% endequation %} כך ש-{% equation %}r^{2}>2{% endequation %} ונראה שלא ייתכן ש-{% equation %}r=\sup A{% endequation %}; נעשה את זה על ידי מציאת {% equation %}d<r{% endequation %} שהוא חסם מלעיל של {% equation %}A{% endequation %} - ובשביל זה מספיק למצוא {% equation %}d<r{% endequation %} כך ש-{% equation %}d^{2}>2{% endequation %} כי אז לכל {% equation %}q\in A{% endequation %} שמקיים {% equation %}q>0{% endequation %} יתקיים {% equation %}q^{2}<d^{2}{% endequation %} וראינו שאפשר להסיק מזה {% equation %}q<d{% endequation %} (אני לא טורח לטפל ב-{% equation %}r{% endequation %} שלילי כי אם {% equation %}r<0{% endequation %} הוא בוודאי לא חסם מלעיל של {% equation %}A{% endequation %} שכוללת את 0).

איך אני אמצא את {% equation %}d{% endequation %} ואעשה את זה בצורה שלא תהיה טכנית ויבשה? ובכן, בואו נחשוב על הסיטואציה בתור נסיון <strong>לקרב</strong> את {% equation %}\sqrt{2}{% endequation %} באמצעות שיטת הקירוב היפהפיה של הרון מאלכסנדריה. הרעיון של השיטה הוא זה: נניח שאנחנו רוצים למצוא שורש למספר {% equation %}N{% endequation %}. בואו נבנה סדרה {% equation %}a_{1},a_{2},a_{3},\ldots{% endequation %} של קירובים לשורש הזה. נתחיל עם מספר כלשהו {% equation %}a_{1}{% endequation %} שיהיה קירוב גס כלשהו של שורש {% equation %}N{% endequation %}. למשל, עבור {% equation %}N=2{% endequation %} אפשר לקחת {% equation %}a_{1}=4{% endequation %}. עכשיו נתחיל <strong>לשפר</strong> את הקירוב על ידי הפעלה נשנית של הכלל הבא:

{% equation %}a_{n+1}=\frac{1}{2}\left(a_{n}+\frac{N}{a_{n}}\right){% endequation %}

הרעיון פה: ניקח את הקירוב הנוכחי שלנו, ונחלק את {% equation %}N{% endequation %} בו. אם הקירוב הנוכחי היה יוצא <strong>בדיוק</strong> {% equation %}\sqrt{N}{% endequation %} אז החלוקה של {% equation %}N{% endequation %} בקירוב הייתה יוצאת {% equation %}\sqrt{N}{% endequation %} בעצמה. אחרת, יצא לנו מספר קצת שונה - אם למשל {% equation %}a_{n}{% endequation %} הוא גדול מדי מכדי להיות השורש, אז {% equation %}\frac{N}{a_{n}}{% endequation %} ייצא קטן מדי מכדי להיות השורש. ועכשיו אומר הרון - אוקיי, בואו ניקח <strong>ממוצע חשבוני</strong> של שני המספרים הללו - נראה לי שהוא יהיה קרוב יותר לשורש. עבור הדוגמא שלנו עם {% equation %}N=2{% endequation %} ו-{% equation %}a_{1}=4{% endequation %} נקבל {% equation %}a_{2}=\frac{1}{2}\left(4+\frac{1}{2}\right)=\frac{9}{4}=2.25{% endequation %} וזה יותר טוב! אם נמשיך את הסדרה, נקבל התכנסות מהירה בצורה מפתיעה אל {% equation %}\sqrt{2}{% endequation %}:

{% equation %}4,2.25,1.569444\ldots,1.42189\ldots,1.414234\ldots{% endequation %}

אפשר לחשוב על השיטה הזו בתור מקרה פרטי של <strong>אלגוריתם ניוטון-רפסון</strong> והזכרתי אותה פה בעבר <a href="https://gadial.net/2017/08/22/0x5f3759df_part_1/">בפוסט</a> על המעשה המופלא בקבוע המסתורי 0x5f3759df, אבל נראה לי שכבר סטיתי מספיק מהעניין. הפואנטה שלי: אני רוצה בהינתן {% equation %}0<r\in\mathbb{Q}{% endequation %} כך ש-{% equation %}r^{2}>2{% endequation %} לקבל {% equation %}d<r{% endequation %} כך שעדיין {% equation %}2<d^{2}{% endequation %} - זה בדיוק מה ששיטת הרון תיתן לי. אני אגדיר

{% equation %}d=\frac{1}{2}\left(r+\frac{2}{r}\right)=\frac{r}{2}+\frac{1}{r}{% endequation %}

ואקבל {% equation %}d{% endequation %} רציונלי כי {% equation %}r{% endequation %} היה רציונלי. בואו נראה שהוא עובד.

דבר ראשון, קל לראות ש-{% equation %}d<r{% endequation %}, כי מכיוון ש-{% equation %}2<r^{2}{% endequation %} אז נחלק ב-{% equation %}2r{% endequation %} ונקבל {% equation %}\frac{1}{r}<\frac{r}{2}{% endequation %} ולכן 

{% equation %}d=\frac{r}{2}+\frac{1}{r}<\frac{r}{2}+\frac{r}{2}=r{% endequation %}

שנית,

{% equation %}d^{2}=\left(\frac{r}{2}+\frac{1}{r}\right)^{2}=\frac{r^{2}}{4}+1+\frac{1}{r^{2}}{% endequation %}

אנחנו רוצים להראות ש-{% equation %}d^{2}>2{% endequation %}, אז מספיק להראות שאם {% equation %}r^{2}>2{% endequation %} אז {% equation %}\frac{r^{2}}{4}+\frac{1}{r^{2}}>1{% endequation %}. קל לראות את זה בשיטות של תיכון אם מסמנים {% equation %}x=r^{2}{% endequation %}, מקבלים את אי השוויון {% equation %}\frac{x}{4}+\frac{1}{x}>1{% endequation %} שעבור {% equation %}x>0{% endequation %} מתורגם לאי השוויון {% equation %}x^{2}-4x+4>0{% endequation %}. אגף שמאל הוא פרבולה "צוחקת" שנקודת החיתוך הימנית שלה עם ציר {% equation %}x{% endequation %} היא {% equation %}x=2{% endequation %} ולכן היא חיובית לכל {% equation %}x>2{% endequation %}, שזה מה שרצינו.

כל הזוועה הזו הראתה לנו ש-{% equation %}r{% endequation %} הוא לא חסם עליון של {% equation %}A{% endequation %} כי אפשר למצוא חסם מלעיל קטן יותר, {% equation %}d{% endequation %}, אבל התחלנו מההנחה ש-{% equation %}r^{2}>2{% endequation %}. אולי בכלל החסם הטוב ביותר מקיים {% equation %}r^{2}<2{% endequation %}? כלומר, הוא איבר של {% equation %}A{% endequation %} בעצמו? אולי יש ב-{% equation %}A{% endequation %} איבר מקסימלי?

במקרה הזה לנסות להשתמש בנוסחת הרון לא עובד (אם אני אגדיר {% equation %}d=\frac{r}{2}+\frac{1}{r}{% endequation %} אני אקבל {% equation %}d^{2}>2{% endequation %}) וכבר אין לי רעיונות לדברים נחמדים להראות אז בואו נעשה את זה בכוח: נגדיר {% equation %}d=r+\varepsilon{% endequation %} כשהרעיון הוא שנקבע את {% equation %}\varepsilon{% endequation %} להיות מספר חיובי קטן ותכף נראה כמה קטן. אז 

{% equation %}d^{2}=r^{2}+2r\varepsilon+\varepsilon^{2}{% endequation %}

ולכן כדי שיתקיים {% equation %}d^{2}<2{% endequation %} צריך שיתקיים {% equation %}\left(2r+\varepsilon\right)\varepsilon<2-r^{2}{% endequation %}. אם אני אוודא ש-{% equation %}\varepsilon<r{% endequation %} אז מספיק לי אפילו למצוא {% equation %}\varepsilon{% endequation %} שעבורו {% equation %}\left(2r+\varepsilon\right)\varepsilon<3r\varepsilon<2-r^{2}{% endequation %}. עכשיו, {% equation %}2-r^{2}{% endequation %} הוא מספר קבוע וגם {% equation %}3r{% endequation %} הוא מספר קבוע, אז אפשר להשתמש בארכימדיות של {% equation %}\mathbb{Q}{% endequation %} כדי למצוא {% equation %}\varepsilon{% endequation %} מתאים.

<h3>סיום זריז לפני הגרנד פינאלה</h3>

אם לסכם את מה שראינו בדוגמא - ב-{% equation %}\mathbb{Q}{% endequation %} יש קבוצות לא ריקות וחסומות בלי חסם עליון, אבל כאלו שיוצרות אצלנו תחושה חזקה ש<strong>אמור</strong> להיות להן חסם עליון. שאפילו בלי להכיר את {% equation %}\mathbb{R}{% endequation %}, יש איזה איבר קונקרטי אחד שאנחנו <strong>מצפים</strong> שיהיה החסם העליון שלהן, וזה שאין כזה - זה מרגיש לנו כמו "חור" בציר המספרים, שתכונת השלמות באה לסתום.

זו אינטואיציה טובה; היא תוביל לאחת משתי הבניות הפורמליות של הממשיים שאני הולך להציג, זו של <strong>חתכי דדקינד</strong>. כרגע, כזכור, אני עדיין לא בונה שום דבר - אני רק שואל את עצמי אילו תכונות אני <strong>רוצה</strong> שיהיו לממשיים. זה מעביר אותנו ישירות אל החלק הבא והאחרון.

<h2>ה</h2>

<h3>מה אני רוצה עכשיו?</h3>

ההגדרה שלי בתחילת הפוסט הייתה כזכור "השדה הסדור השלם". מה זה שדה - ראינו. מה זה שדה סדור - ראינו. מה זה שדה סדור שלם - ראינו. מה שעדיין לא ברור הוא התפקיד של האות ה' בביטוי הזה. אות קטנה, משמעות גדולה: כשאני מדבר על "<strong>ה</strong>שדה הסדור השלם" הכוונה היא <strong>שקיים</strong> שדה כזה והוא <strong>יחיד</strong>. כלומר, כשאני משתמש בהגדרה הזו אני טוען טענת קיום ויחידות, שהיא משהו שצריך <strong>להוכיח</strong>. במובן הזה ההגדרה שלי היא יותר מסתם הגדרה - היא גם הבטחה.

מצד שני, זה מרגיש שאני קצת מרמה כי אני לא <strong>באמת</strong> מסביר עד הסוף איך אפשר לקבל לידיים את האובייקט שאני מגדיר. כאמור, זה דבר די סטנדרטי במתמטיקה; אנחנו צריכים להבדיל בין הגדרה אקסיומטית שמתארת תכונות רלוונטיות של אובייקטים שאחר כך אפשר להשתמש בהן כדי להוכיח תכונות נוספות של האובייקטים, וההוכחה תהיה תקפה <strong>לכל</strong> אובייקט שמקיים את התכונות - ובין מה שאני מעדיף לקרוא לו <strong>בנייה</strong> שמתאר איך מייצרים את האובייקט מתוך אובייקטים פשוטים יותר.

ראינו סוג של בניה בפוסט הקודם, עם הייצוגים העשרוניים; זו לא הייתה בניה מלאה כי הגדרתי את האובייקטים של הקבוצה אבל לא את פעולות החיבור והכפל ולא את האופן שבו מוגדר יחס הסדר (כל אלו לא טריוויאליים). אני אראה בפוסט הבא שתי בניות נוספות, שאותן אציג עד הסוף. יותר מזה - שתי הבניות <strong>לא</strong> הולכות לבנות את אותו הדבר, במובן זה שאחת מהן תיצור לנו אוסף של קבוצות של רציונליים, ואילו השניה תיצור אוסף של מחלקות שקילות של סדרות של רציונליים. אלו שני אובייקטים שונים, מה שמעלה את השאלה - מי מביניהם יהיה {% equation %}\mathbb{R}{% endequation %} "האמיתי"? התשובה היא ששניהם הם {% equation %}\mathbb{R}{% endequation %} האמיתי, במובן זה ששניהם מקיימים את התכונות המהותיות שאנחנו מצפים להן מ-{% equation %}\mathbb{R}{% endequation %} - שניהם יהיו <strong>שדה סדור שלם</strong> ויותר מכך - <strong>שביחס לתכונות הללו</strong> הם יהיו בדיוק אותו אובייקט עד כדי שינוי שמות האיברים. זו המהות של טיעון ה"יחידות", ואותו אני אוכל להוכיח כאן, אפילו לפני שאני מציג בניות אלו ואחרות. פורמלית, אני אוכיח שאם {% equation %}\mathbb{F}_{1},\mathbb{F}_{2}{% endequation %} הם שני שדות סדורים שלמים, אז הם <strong>איזומורפיים</strong>, עם ההגדרה הבאה של איזומורפיזם:

{% equation %}f:\mathbb{F}_{1}\to\mathbb{F}_{2}{% endequation %} הוא <strong>איזומורפיזם</strong> של שדות סדורים אם {% equation %}f{% endequation %} פונקציה חד-חד-ערכית ועל ומתקיים

<ul> <li>{% equation %}f\left(x+y\right)=f\left(x\right)+f\left(y\right){% endequation %}</li>


<li>{% equation %}f\left(x\cdot y\right)=f\left(x\right)\cdot f\left(y\right){% endequation %}</li>


<li>{% equation %}x<y{% endequation %} אם ורק אם {% equation %}f\left(x\right)<f\left(y\right){% endequation %}</li>

</ul>

אני אזכיר מה "חד-חד-ערכית" ו"על" אומרים (ויש לי גם <a href="https://gadial.net/2020/05/15/invertible_functions/">פוסט</a>): {% equation %}f:A\to B{% endequation %} היא חח"ע אם {% equation %}f\left(x\right)=f\left(y\right){% endequation %} גורר {% equation %}x=y{% endequation %}, כלומר אם קלטים שונים מתמפים לפלטים שונים. {% equation %}f:A\to B{% endequation %} היא על אם לכל {% equation %}b\in B{% endequation %} קיים {% equation %}a\in A{% endequation %} כך ש-{% equation %}f\left(a\right)=b{% endequation %}, כלומר כל איבר של {% equation %}B{% endequation %} מתקבל כפלט של {% equation %}f{% endequation %} על משהו מ-{% equation %}A{% endequation %}. זה שפונקציה היא גם חח"ע וגם על אומר שאפשר לחשוב עליה כאילו היא מסדרת את אברי {% equation %}A{% endequation %} ו-{% equation %}B{% endequation %} בזוגות-זוגות - לכל איבר של {% equation %}a{% endequation %} יש בן זוג אחד ויחיד מ-{% equation %}b{% endequation %}, וההפך. זה מאפשר לנו לדמיין ש-{% equation %}B{% endequation %} היא פשוט "אברי {% equation %}A{% endequation %} עם שמות אחרים": לוקחים את {% equation %}A{% endequation %}, מחליפים את השם של כל איבר {% equation %}a\in A{% endequation %} ב-{% equation %}f\left(a\right){% endequation %}, מקבלים את {% equation %}B{% endequation %}.

אם על {% equation %}A,B{% endequation %} יש עוד <strong>מבנה</strong> מלבד סתם איברים, האשליה הזו של שינוי השם עשוי להתנפץ. למשל, אם {% equation %}A=\mathbb{N}{% endequation %} ו-{% equation %}B=\mathbb{Z}{% endequation %} אז פונקציה חח"ע ועל {% equation %}f:A\to B{% endequation %} היא {% equation %}f\left(n\right)=\begin{cases} \frac{n}{2} & n\equiv_{2}0\\ -\frac{n+1}{2} & n\equiv_{2}1 \end{cases}{% endequation %}. מה ש-{% equation %}f{% endequation %} עושה הוא להעביר את סדרת הטבעיים {% equation %}0,1,2,3,\ldots{% endequation %} אל סדרת השלמים {% equation %}0,-1,1,-2,2,\ldots{% endequation %}. זו התאמה חח"ע ועל, אבל היא ממש לא מתנהגת יפה עם המבנה הנוסף שיש לנו על {% equation %}\mathbb{N}{% endequation %}. למשל, {% equation %}1+1=2{% endequation %} ולכן אם {% equation %}f{% endequation %} היא בסך הכל שינוי שם היינו מצפים שיתקיים {% equation %}f\left(1\right)+f\left(1\right)=f\left(2\right){% endequation %}. אבל {% equation %}f\left(2\right)=1{% endequation %} ואילו {% equation %}f\left(1\right)=-1{% endequation %} ולכן {% equation %}f\left(1\right)+f\left(1\right)=-2=f\left(3\right)\ne f\left(2\right){% endequation %}, כך שהאשליה שיש כאן שינוי שמות ותו לא מתנפצת ברגע שבו אנחנו מצפים משינוי השמות לשחק יפה עם המבנה הנוסף שיש על הקבוצות.

<h3>מה הולכים להוכיח ואיך</h3>

על שדה סדור יש שלושה מבנים: פעולת החיבור, פעולת הכפל ויחס הסדר {% equation %}<{% endequation %} (או באופן שקול, הקבוצה {% equation %}P{% endequation %}; במקום הדרישה השלישית היינו יכולים לדרוש {% equation %}f\left(P_{1}\right)=P_{2}{% endequation %}). האתגר שלי יהיה להציג פונקציה שמשחקת יפה עם כולם.

הנה בגדול הרעיון:

<ul> <li>ראשית נראה שכל שדה סדור מכיל עותק של {% equation %}\mathbb{Q}{% endequation %} וששני העותקים הללו איזומורפיים.</li>


<li>אחר כך נראה שכל שדה סדור <strong>שלם</strong> הוא ארכימדי.</li>


<li>המסקנה מזה תהיה שאפשר להציג כל איבר בשדה בתור {% equation %}\sup{% endequation %} של קבוצה של רציונליים, וזה יאפשר לנו להרחיב את האיזומורפיזם של הרציונליים לאיזומורפיזם של כל השדה.</li>

</ul>

בעצם, בואו נתחיל מזה שכל שדה סדור שלם הוא ארכימדי, זו תוצאה קלילה להוכחה וככה היא לא תקטע את הרצף של מה שנעשה אחר כך. ניקח שדה סדור שלם {% equation %}\mathbb{F}{% endequation %} כלשהו. כבר ראינו שבגלל שהשדה סדור, הוא חייב להיות ממציין 0, כלומר כל האיברים {% equation %}1,1+1,1+1+1,\ldots{% endequation %} קיימים ושונים זה מזה - במילים אחרות, יש בתוך {% equation %}\mathbb{F}{% endequation %} עותק של {% equation %}\mathbb{Z}{% endequation %}. עכשיו, אם {% equation %}\mathbb{F}{% endequation %} <strong>לא ארכימדי</strong>, מה זה אומר? ארכימדיות פירושה שלכל {% equation %}a\in\mathbb{F}{% endequation %} קיים {% equation %}n\in\mathbb{Z}{% endequation %} כך ש-{% equation %}a<n{% endequation %}. 

אם ניקח את השלילה של הטענה הזו נקבל שקיים {% equation %}a\in\mathbb{F}{% endequation %} כך שלכל {% equation %}n\in\mathbb{Z}{% endequation %} מתקיים {% equation %}n\le a{% endequation %}. במילים אחרות, {% equation %}a{% endequation %} הוא <strong>חסם מלעיל</strong> של {% equation %}\mathbb{Z}{% endequation %}, והשלמות של {% equation %}\mathbb{F}{% endequation %} אומרת ש-{% equation %}d=\sup\mathbb{Z}{% endequation %} קיים. עכשיו, בואו ניקח {% equation %}n\in\mathbb{Z}{% endequation %} כלשהו. מכיוון שגם {% equation %}n+1\in\mathbb{Z}{% endequation %}, אנחנו יודעים ש-{% equation %}n+1<d{% endequation %}, כלומר {% equation %}n<d-1{% endequation %}, וזה נכון <strong>לכל</strong> {% equation %}n\in\mathbb{Z}{% endequation %} ולכן גם {% equation %}d-1{% endequation %} חסם מלעיל של {% equation %}\mathbb{Z}{% endequation %}, בסתירה למינימליות של {% equation %}d{% endequation %}. כלומר - בשדה סדור, או ש-{% equation %}\mathbb{Z}{% endequation %} לא חסומה (כלומר, השדה ארכימדי) או שהשדה לא שלם, אין עוד אפשרויות.

עכשיו בואו נדבר על {% equation %}\mathbb{Q}{% endequation %}. ראינו כבר במהלך הפוסט שיש ב-{% equation %}\mathbb{F}{% endequation %} קבוצה שזהה ל-{% equation %}\mathbb{Q}{% endequation %}, אבל בואו נעשה את זה שוב, הכי מסודר שאפשר. מה שאקסיומות השדה נותנות לנו הוא קיום של איברים {% equation %}0,1\in\mathbb{F}{% endequation %}. שימו לב שהאיברים הללו הם <strong>לא</strong> המספרים 0,1; הם סתם שני איברים של {% equation %}\mathbb{F}{% endequation %} שזכו לסימון מיוחד. אז בואו כרגע ניתן להם סימון אחר: את האדיש החיבורי אסמן ב-{% equation %}\mathcal{O}{% endequation %} ואת האדיש הכפלי אסמן ב-{% equation %}\mathcal{I}{% endequation %}. מה שאני יודע לומר הוא שלכל {% equation %}a\in\mathbb{F}{% endequation %} מתקיים {% equation %}a+\mathcal{O}=a{% endequation %} ו-{% equation %}a\cdot\mathcal{I}=a{% endequation %}. עכשיו בואו נבנה מזה את {% equation %}\mathbb{Q}{% endequation %}.

<h3>בונים את הרציונליים (מתוך השדה הקיים)</h3>

ראשית, לכל מספר טבעי {% equation %}n\in\mathbb{N}{% endequation %} בואו נגדיר איבר {% equation %}\mathcal{Z}_{n}\in\mathbb{F}{% endequation %}. נעשה את זה רקורסיבית: {% equation %}\mathcal{Z}_{0}=\mathcal{O}{% endequation %} ואם {% equation %}\mathcal{Z}_{n}{% endequation %} כבר הוגדר, נגדיר {% equation %}\mathcal{Z}_{n+1}=\mathcal{Z}_{n}+\mathcal{I}{% endequation %}.

עכשיו אני רוצה לטעון ש-{% equation %}\mathcal{Z}_{k}+\mathcal{Z}_{n}=\mathcal{Z}_{k+n}{% endequation %}. ההוכחה תכה אותנו בכזה הלם של טרחנות שנוותר על המשך ההוכחות בסגנון, כי זה הכל אותו דבר (מי שמכירים את ההגדרות הפורמליות של טבעיים ירגישו בוודאי בבית עם ההוכחה הזו). אני אוכיח את הטענה באינדוקציה על {% equation %}n{% endequation %}. אם {% equation %}n=0{% endequation %} אז על פי הגדרה, {% equation %}\mathcal{Z}_{0}=\mathcal{O}{% endequation %} ולכן 

{% equation %}\mathcal{Z}_{k}+\mathcal{Z}_{0}=\mathcal{Z}_{k}+\mathcal{O}=\mathcal{Z}_{k}=\mathcal{Z}_{k+0}{% endequation %}

ואם הטענה כבר הוכחה עבור {% equation %}n{% endequation %} ואנחנו רוצים להוכיח אותה עבור {% equation %}n+1{% endequation %}, נשתמש בכך ש-{% equation %}\mathcal{Z}_{n+1}=\mathcal{Z}_{n}+\mathcal{I}{% endequation %} ונקבל

{% equation %}\mathcal{Z}_{k}+\mathcal{Z}_{n+1}=\mathcal{Z}_{k}+\left(\mathcal{Z}_{n}+\mathcal{I}\right)=\left(\mathcal{Z}_{k}+\mathcal{Z}_{n}\right)+\mathcal{I}={% endequation %}

{% equation %}=\mathcal{Z}_{k+n}+\mathcal{I}=\mathcal{Z}_{\left(k+n\right)+1}=\mathcal{Z}_{k+\left(n+1\right)}{% endequation %}

אני לא חושב שקיימת אפשרות להיות יותר פדנט מזה, אבל לא הכל נורא! עכשיו אנחנו רואים יפה וברור שבהוכחה הזו משתמשים <strong>באסוציאטיביות החיבור</strong> ("חוק הקיבוץ") גם ב-{% equation %}\mathbb{F}{% endequation %} וגם ב-{% equation %}\mathbb{N}{% endequation %}. בלי אסוציאטיביות, שום דבר לא היה עובד! אנחנו לא תמיד מעריכים עד כמה היקום היה קורס בלי אסוציאטיביות.

בכל מקרה, עכשיו אני ארשה לעצמי לנופף ידיים בפראות בהמשך. לא קשה להוכיח גם ש-{% equation %}\mathcal{Z}_{k}\cdot\mathcal{Z}_{n}=\mathcal{Z}_{k\cdot n}{% endequation %} ולא קשה גם להוכיח ש-{% equation %}\mathcal{Z}_{k}<\mathcal{Z}_{n}{% endequation %} אם ורק אם {% equation %}k<n{% endequation %}, הכל עם אינדוקציות מזעזעות. לכן מה שעשיתי כאן בעצם היה להגדיר פונקציה {% equation %}f:\mathbb{N}\to\mathbb{F}{% endequation %} על ידי {% equation %}f\left(n\right)=\mathcal{Z}_{n}{% endequation %}, והפונקציה הזו מקיימת את שלוש הדרישות שלי:

<ul> <li>{% equation %}f\left(n+k\right)=f\left(n\right)+f\left(k\right){% endequation %}</li>


<li>{% equation %}f\left(n\cdot k\right)=f\left(n\right)\cdot f\left(k\right){% endequation %}</li>


<li>{% equation %}n<k{% endequation %} אם ורק אם {% equation %}f\left(n\right)<f\left(k\right){% endequation %}</li>

</ul>

בנוסף, זו פונקציה חח"ע, כי אם {% equation %}\mathcal{Z}_{n}=\mathcal{Z}_{k}{% endequation %} עבור {% equation %}k<n{% endequation %} אז נשתמש בטענה הנכונה תמיד {% equation %}\mathcal{Z}_{k}+\mathcal{Z}_{n-k}=\mathcal{Z}_{n}{% endequation %}, נעביר את {% equation %}\mathcal{Z}_{k}{% endequation %} אגף, נשתמש ב-{% equation %}\mathcal{Z}_{n}=\mathcal{Z}_{k}{% endequation %} ונקבל {% equation %}\mathcal{Z}_{n-k}=\mathcal{O}{% endequation %}, ומכיוון ש-{% equation %}n-k>0{% endequation %} המסקנה היא שקיבלנו סכום של {% equation %}\mathcal{I}{% endequation %}-ים שמסתכם לאפס - זאת בסתירה למה שכבר ראינו, שהשדה הוא ממציין 0.

המסקנה היא ש-{% equation %}f{% endequation %} היא פונקציית "אותו הדבר רק בסימון אחר" מצויינת, ולכן אפשר לנטוש את כל פיאסקו הכתיבה של דברים בתור {% equation %}\mathcal{Z}_{n}{% endequation %} וכאלו ופשוט לכתוב {% equation %}0,1,2\ldots,n,\ldots{% endequation %} עבור האיברים שהגדרתי פה ולהתייחס אליהם כאילו הם "באמת" הטבעיים.

מרגע שיש לנו את זה, אפשר להרחיב את הגדרת {% equation %}f{% endequation %}. ראשית, נגדיר אותה על כל {% equation %}\mathbb{Z}{% endequation %}, כלומר צריך להסביר איך היא מתנהגת גם על השליליים, איברים מהצורה {% equation %}-n{% endequation %} כך ש-{% equation %}n\in\mathbb{N}{% endequation %}: {% equation %}f\left(-n\right)=-n{% endequation %}. זו נראית הגדרה כמעט ריקה, אבל העיקרון לא טריוויאלי: אנחנו מזמנים את {% equation %}\mathcal{Z}_{n}{% endequation %}, ואז מפעילים את האקסיומה של {% equation %}\mathbb{F}{% endequation %} שאומרת שקיים לו נגדי, שמסומן {% equation %}-\mathcal{Z}_{n}{% endequation %}, וזה מה ש-{% equation %}f{% endequation %} תחזיר - רק שכאמור, כבר הפסקתי עם השטות של כתיבת {% equation %}\mathcal{Z}_{n}{% endequation %} ואני כותב {% equation %}n{% endequation %} וזהו.

גם על ההגדרה הזו צריך להוכיח שהיא מקיימת את שלוש התכונות שלמעלה. זה עובד. תסמכו עלי. בואו נרוץ אל הרחבת {% equation %}f{% endequation %} לכל {% equation %}\mathbb{Q}{% endequation %}. מה שמדגדג לומר הוא שנגדיר לכל {% equation %}a,b\in\mathbb{Z}{% endequation %} כך ש-{% equation %}b\ne0{% endequation %} את ההגדרה הבאה:

{% equation %}f\left(\frac{a}{b}\right)=a\cdot b^{-1}{% endequation %}

כלומר, אנחנו לוקחים את האיבר ב-{% equation %}\mathbb{F}{% endequation %} שמתאים ל-{% equation %}a{% endequation %} והאיבר ב-{% equation %}\mathbb{F}{% endequation %} שמתאים ל-{% equation %}b{% endequation %}, משתמשים בזה שהאיבר שמתאים ל-{% equation %}b{% endequation %} יהיה שונה מ-0 כי {% equation %}b{% endequation %} שונה מאפס ו-{% equation %}f{% endequation %} חח"ע, משתמשים באקסיומות השדה כדי למצוא הופכי ל-{% equation %}b{% endequation %} הזה וכופלים אותו ב-{% equation %}a{% endequation %}. אין שום בעיה בהגדרה הזו אבל צריך לוודא שהיא מה שנקרא <strong>מוגדרת היטב</strong> כי קיימת הסכנה ש<strong>אותו מספר רציונלי</strong> יניב פלטים שונים של {% equation %}f{% endequation %}, כתלות בייצוג שלו. כלומר, אני רוצה להראות למשל ש-{% equation %}f\left(\frac{1}{2}\right)=f\left(\frac{2}{4}\right){% endequation %}. זה לא לגמרי מובן מאליו כי באגף ימין של ההגדרה אין מספרים אלא יש איברים של {% equation %}\mathbb{F}{% endequation %} ולכו תדעו איזה מוזרויות יש להם, אבל למרבה המזל ההוכחה די פשוטה.

נניח שברציונליים, {% equation %}\frac{a}{b}=\frac{c}{d}{% endequation %}. כלומר, {% equation %}ad=bc{% endequation %}. זו משוואה של מספרים ב-{% equation %}\mathbb{Z}{% endequation %}, ולכן היא נכונה גם בתוך {% equation %}\mathbb{F}{% endequation %}. לכן אפשר לקחת את {% equation %}ad=bc{% endequation %} בתוך {% equation %}\mathbb{F}{% endequation %} ולכפול את שני האגפים ב-{% equation %}b^{-1}{% endequation %} וב-{% equation %}d^{-1}{% endequation %} ולקבל {% equation %}ab^{-1}=cd^{-1}{% endequation %}, כלומר {% equation %}f\left(\frac{a}{b}\right)=ab^{-1}=cd^{-1}=f\left(\frac{c}{d}\right){% endequation %}, שזה מה שרצינו. אנחנו עדיין צריכים להוכיח ששאר התכונות של {% equation %}f{% endequation %} מתקיימות - זה כאמור תרגיל טוב שאני לא הולך לעשות כאן. קיבלנו {% equation %}f:\mathbb{Q}\to\mathbb{F}{% endequation %} שהיא חח"ע ומכבדת את המבנה של השדה. במתמטית קוראים לזה <strong>שיכון</strong> (להבדיל מאיזומורפיזם; כי כאן {% equation %}f{% endequation %} לא על כל {% equation %}\mathbb{F}{% endequation %}). מכאן ואילך אני יכול להתייחס ל-{% equation %}\mathbb{F}{% endequation %} כאילו יש עותק של {% equation %}\mathbb{Q}{% endequation %} שיושב בתוכה, כמו שבעצם עשיתי גם קודם.

עכשיו הגענו סוף סוף אל הפאנץ' האחרון: יש לי שני שדות סדורים שלמים {% equation %}\mathbb{F}_{1},\mathbb{F}_{2}{% endequation %}. אני רוצה להגדיר {% equation %}g:\mathbb{F}_{1}\to\mathbb{F}_{2}{% endequation %} שהיא חח"ע, על ומכבדת את המבנה של השדה הסדור. איך אני אעשה את זה? התשובה היא שכל אחד ואחד מהאיברים של השדות הללו הוא <strong>חסם עליון של קבוצה של רציונליים</strong> ואני הולך לבנות את {% equation %}g{% endequation %} כך שהיא מעבירה את החסם העליון של קבוצה ב-{% equation %}\mathbb{F}_{1}{% endequation %} אל החסם העליון של <strong>אותה קבוצה</strong> ב-{% equation %}\mathbb{F}_{2}{% endequation %}.

בואו ננסח את זה פורמלית. אנחנו יודעים שיש תת-שדות {% equation %}\mathbb{Q}_{1}\subseteq\mathbb{F}_{1}{% endequation %} ו-{% equation %}\mathbb{Q}_{2}\subseteq\mathbb{F}_{2}{% endequation %} שאיזומורפים לרציונליים ובפרט איזומורפים זה לזה, עם פונקציה {% equation %}f:\mathbb{Q}_{1}\to\mathbb{Q}_{2}{% endequation %} שהיא איזומורפיזם. אני הולך <strong>להרחיב</strong> את {% equation %}f{% endequation %} הזו כדי להגדיר איזומורפיזם {% equation %}f:\mathbb{F}_{1}\to\mathbb{F}_{2}{% endequation %} באופן הבא: לכל {% equation %}x\in\mathbb{F}_{1}{% endequation %} נגדיר קבוצה {% equation %}A_{x}\subseteq\mathbb{F}_{2}{% endequation %} (כלומר, של איברים <strong>בשדה השני</strong>) על ידי 

{% equation %}A_{x}=\left\{ f\left(q\right)\ |\ q\in\mathbb{Q}_{1}\wedge q<x\right\} {% endequation %} 

עכשיו אני אגדיר {% equation %}f\left(x\right)=\sup A_{x}{% endequation %}. זהו, זו כל ההגדרה - ועכשיו תגיע המהומה הגדולה מכולן, להראות שההגדרה הזו עובדת. 

<h3>המהומה הגדולה מכולן</h3>

מה זה אומר, להראות שההגדרה עובדת? צריך להוכיח את כל הדברים הבאים:

<ul> <li>{% equation %}f{% endequation %} מוגדרת היטב (לכל קלט קיים פלט יחיד)</li>


<li>{% equation %}f{% endequation %} חד-חד-ערכית</li>


<li>{% equation %}f{% endequation %} על</li>


<li>{% equation %}f\left(x+y\right)=f\left(x\right)+f\left(y\right){% endequation %}</li>


<li>{% equation %}f\left(x\cdot y\right)=f\left(x\right)\cdot f\left(y\right){% endequation %}</li>


<li>{% equation %}x<y{% endequation %} אם ורק אם {% equation %}f\left(x\right)<f\left(y\right){% endequation %}</li>

</ul>

ראשית צריך להראות ש-{% equation %}f{% endequation %} מוגדרת היטב. יש כאן שתי סכנות: גם סכנה של הגדרה כפולה, וגם סכנה שיהיו קלטים שעבורם {% equation %}f{% endequation %} לא מוגדרת. נתחיל עם ההגדרה הכפולה: הרי לקחתי פונקציה <strong>קיימת</strong> {% equation %}f:\mathbb{Q}_{1}\to\mathbb{Q}_{2}{% endequation %} והגדרתי באמצעותה פונקציה <strong>חדשה</strong> {% equation %}f:\mathbb{F}_{1}\to\mathbb{F}_{2}{% endequation %}. אני רוצה להראות שאם {% equation %}x\in\mathbb{Q}_{1}{% endequation %} אז שתי ההגדרות מסכימות זו עם זו על {% equation %}x{% endequation %}, כלומר ש-{% equation %}f\left(x\right)=\sup A_{x}{% endequation %} (אגף שמאל הוא ההגדרה "המקורית", אגף ימין הוא ההגדרה החדשה). אפשר ובצדק לשאול למה לא פשוט להגדיר פונקציה <strong>חדשה</strong> בעזרת {% equation %}f{% endequation %} אבל לקרוא לפונקציה החדשה הזו {% equation %}g{% endequation %} ואז לדלג על השלב הזה; התשובה היא שאני אסתמך על כך שהפונקציה שבניתי מרחיבה את {% equation %}f{% endequation %} המקורית בהמשך ההוכחה, כשנצטרך להוכיח שהפונקציה החדשה היא על.

נתחיל עם להראות ש-{% equation %}\sup A_{x}\le f\left(x\right){% endequation %} עבור {% equation %}x\in\mathbb{Q}_{1}{% endequation %}. בשביל זה מספיק להראות ש-{% equation %}f\left(x\right){% endequation %} הוא חסם מלעיל של {% equation %}A_{x}{% endequation %} כי הסופרמום של {% equation %}A_{x}{% endequation %} קטן או שווה לכל חסם מלעיל שלה. אז ניקח איבר כללי ב-{% equation %}A_{x}{% endequation %}, כלומר איבר {% equation %}f\left(q\right){% endequation %} כך ש-{% equation %}q<x{% endequation %}, ועכשיו נשתמש בכך ש-{% equation %}f{% endequation %} היא איזומורפיזם, כלומר משמרת סדר, כלומר {% equation %}f\left(q\right)<f\left(x\right){% endequation %}, שהוא מה שרצינו. עכשיו, בואו נראה שלא ייתכן ש-{% equation %}\sup A_{x}<f\left(x\right){% endequation %}: במקרה הזה, הצפיפות של {% equation %}\mathbb{Q}_{2}{% endequation %} ב-{% equation %}\mathbb{F}_{2}{% endequation %} נותנת לנו איבר {% equation %}p^{\prime}\in\mathbb{Q}_{2}{% endequation %} כך ש-{% equation %}\sup A_{x}<p^{\prime}<f\left(x\right){% endequation %}. במקום לעבוד עם {% equation %}p^{\prime}{% endequation %} ישירות, יהיה לי כאן ובהמשך יותר קל לדבר עליו בתור {% equation %}f\left(p\right){% endequation %} עבור {% equation %}p\in\mathbb{Q}_{1}{% endequation %} - אני יודע ש-{% equation %}p{% endequation %} כזה קיים כי {% equation %}f{% endequation %} היא איזומורפיזם ולכן פשוט {% equation %}p=f^{-1}\left(p^{\prime}\right){% endequation %}.

אם כן, נתון לי {% equation %}\sup A_{x}<f\left(p\right)<f\left(x\right){% endequation %}. אי השוויון {% equation %}f\left(p\right)<f\left(x\right){% endequation %} פירושו {% equation %}p<x{% endequation %} (שוב, כי {% equation %}f{% endequation %} איזומורפיזם ובפרט משמרת סדר), כלומר {% equation %}f\left(p\right)\in A_{x}{% endequation %} על פי הגדרת {% equation %}A_{x}{% endequation %} ולכן {% equation %}f\left(p\right)\le\sup A_{x}{% endequation %} - סתירה לנתון {% equation %}\sup A_{x}<f\left(p\right){% endequation %}. זה מראה לנו ש-{% equation %}\sup A_{x}=f\left(x\right){% endequation %}.

זה עדיין לא מסיים את ההוכחה ש-{% equation %}f{% endequation %} מוגדרת היטב כי יש עוד סכנה: שעבור {% equation %}x{% endequation %} כלשהו, {% equation %}A_{x}{% endequation %} תהיה קבוצה נטולת סופרמום. אני כמובן משתמש פה חזק בכך ש-{% equation %}\mathbb{F}_{2}{% endequation %} מקיים את אקסיומת השלמות (ומתי אשתמש בה עבור {% equation %}\mathbb{F}_{1}{% endequation %}?) אבל גם עם אקסיומת השלמות אני עדיין צריך להשתכנע ש-{% equation %}A_{x}{% endequation %} לא ריקה (הארכימידיות של {% equation %}\mathbb{F}_{2}{% endequation %} נותנת את זה מיד) וש-{% equation %}A_{x}{% endequation %} חסומה. החסימות נובעת מהארכימידית של {% equation %}\mathbb{F}_{1}{% endequation %}, שנותנת לנו {% equation %}n{% endequation %} כך ש-{% equation %}x<n{% endequation %}. אז {% equation %}f\left(n\right){% endequation %} הוא חסם מלעיל של {% equation %}A_{x}{% endequation %}, כי אם ניקח איבר כלשהו ב-{% equation %}A_{x}{% endequation %} הוא מהצורה {% equation %}f\left(q\right){% endequation %} כך ש-{% equation %}q<x{% endequation %} ולכן מטרנזיטיביות יחס הסדר, {% equation %}q<n{% endequation %} ומכך ש-{% equation %}f{% endequation %} היא איזומורפיזם נקבל {% equation %}f\left(q\right)<f\left(n\right){% endequation %}. זה מסיים את הטענה ש-{% equation %}g{% endequation %} מוגדרת היטב, כי ראינו שאכן {% equation %}\sup A_{x}{% endequation %} קיים.

כדי לראות ש-{% equation %}f{% endequation %} חח"ע, בואו ניקח {% equation %}x\ne y\in\mathbb{F}_{1}{% endequation %} כלשהם ונראה ש-{% equation %}f\left(x\right)\ne f\left(y\right){% endequation %}. בלי הגבלת הכלליות אני אניח ש-{% equation %}x<y{% endequation %}, ומהצפיפות של הרציונליים קיימים {% equation %}p_{1},p_{2}\in\mathbb{Q}_{1}{% endequation %} כך ש-{% equation %}x<p_{1}<p_{2}<y{% endequation %}. עכשיו, {% equation %}f\left(p_{1}\right){% endequation %} הוא חסם מלעיל של {% equation %}A_{x}{% endequation %}, כי אם {% equation %}q<x{% endequation %} אז בפרט {% equation %}q<x<p_{1}{% endequation %} ולכן {% equation %}f\left(q\right)<f\left(p_{1}\right){% endequation %} (כבר ראינו לפני רגע את אותו טיעון) ולכן {% equation %}\sup A_{x}\le f\left(p_{1}\right){% endequation %} (כי הסופרמום הוא החסם מלעיל הקטן ביותר). בנוסף, {% equation %}p_{2}<y{% endequation %} פירושו על פי הגדרה {% equation %}f\left(p_{2}\right)\in A_{y}{% endequation %} ולכן {% equation %}f\left(p_{2}\right)\le\sup A_{y}{% endequation %} ולכן

{% equation %}f\left(x\right)=\sup A_{x}\le f\left(q\right)<f\left(p\right)\le\sup A_{y}=f\left(y\right){% endequation %}

כלומר {% equation %}f\left(x\right)<f\left(y\right){% endequation %} ובפרט {% equation %}f\left(x\right)\ne f\left(y\right){% endequation %}. שימו לב שבעצם הוכחנו כבר חצי מהתכונה האחרונה: הראינו שאם {% equation %}x<y{% endequation %} אז {% equation %}f\left(x\right)<f\left(y\right){% endequation %}. אבל למעשה, זה נותן לנו גם את החצי השני: אם {% equation %}f\left(x\right)<f\left(y\right){% endequation %} אבל {% equation %}y\le x{% endequation %} אז {% equation %}f\left(y\right)\le f\left(x\right){% endequation %} וקיבלנו סתירה (כאן אנחנו מסתמכים על כך שיחס הסדר הוא <strong>מלא</strong>; עבור יחס סדר כללי לא מקבלים את שני הכיוונים ביחד).

כדי לראות ש-{% equation %}f{% endequation %} על, בואו ניקח {% equation %}y\in\mathbb{F}_{2}{% endequation %} כלשהו ונמצא {% equation %}x\in\mathbb{F}_{1}{% endequation %} כך ש-{% equation %}f\left(x\right)=y{% endequation %}. לצורך כך, בואו נסתכל על הקבוצה {% equation %}B_{y}=\left\{ q\in\mathbb{Q}_{1}\ |\ f\left(q\right)<y\right\} {% endequation %} - זו הגדרה שמזכירה את זו של {% equation %}A_{x}{% endequation %} ולא במקרה - זה כאילו אני מנסה להגדיר פונקציה בכיוון ההפוך, מ-{% equation %}\mathbb{F}_{2}{% endequation %} אל {% equation %}\mathbb{F}_{1}{% endequation %}, אז גם ברור מה יהיה הצעד הבא: אני ארצה להגדיר {% equation %}x=\sup B_{y}{% endequation %}. בשביל זה אצטרך לראות ש-{% equation %}B_{y}{% endequation %} לא ריקה וחסומה. בשביל שני אלו אני אשתמש בכך ש-{% equation %}f{% endequation %} היא איזומורפיזם, כלומר {% equation %}f^{-1}{% endequation %} קיימת: אני אשתמש בארכימדיות של {% equation %}\mathbb{F}_{2}{% endequation %} כדי לקבל איברים {% equation %}f\left(q_{1}\right)<y<f\left(q_{2}\right){% endequation %} כך ש-{% equation %}q_{1},q_{2}\in\mathbb{Q}_{1}{% endequation %}, ואז {% equation %}q_{1}\in B_{y}{% endequation %} ולכן זו לא קבוצה ריקה, ו-{% equation %}f\left(q_{2}\right){% endequation %} יהיה חסם מלעיל של {% equation %}B_{y}{% endequation %}, כי אם {% equation %}q\in B_{y}{% endequation %} אז {% equation %}f\left(q\right)<y<f\left(q_{2}\right){% endequation %} ולכן בגלל ש-{% equation %}f{% endequation %} משמרת סדר {% equation %}f\left(q\right)<f\left(q_{2}\right){% endequation %} ייתן לנו {% equation %}q<q_{2}{% endequation %}.

הגדרתי את {% equation %}x{% endequation %} אבל עדיין צריך להראות ש-{% equation %}f\left(x\right)=y{% endequation %}. האם ייתכן ש-{% equation %}f\left(x\right)<y{% endequation %}? במקרה כזה, צפיפות הרציונליים תיתן לנו {% equation %}p\in\mathbb{Q}_{1}{% endequation %} כך ש-{% equation %}f\left(x\right)<f\left(p\right)<y{% endequation %}, אבל מכיוון ש-{% equation %}f\left(p\right)<y{% endequation %} הרי ש-{% equation %}p\in B_{y}{% endequation %}, ולכן מכיוון ש-{% equation %}x=\sup B_{y}{% endequation %} אז {% equation %}p\le x{% endequation %} ולכן {% equation %}f\left(p\right)\le f\left(x\right){% endequation %} (זה נובע מכך שכבר הוכחנו שאם {% equation %}a<b{% endequation %} אז {% equation %}f\left(a\right)<f\left(b\right){% endequation %}) וזו סתירה לכך ש-{% equation %}f\left(x\right)<f\left(p\right){% endequation %}. נשאר רק להראות שלא ייתכן {% equation %}y<f\left(x\right){% endequation %}. אם זה כן היה מתקיים, אז היינו מקבלים {% equation %}f^{-1}\left(y\right)<x{% endequation %}, אבל {% equation %}f^{-1}\left(y\right){% endequation %} הוא בעצמו חסם מלעיל של {% equation %}B_{y}{% endequation %} (כי אם {% equation %}f\left(q\right)<y{% endequation %} אז {% equation %}q<f^{-1}\left(y\right){% endequation %}) ולכן {% equation %}f^{-1}\left(y\right)<x{% endequation %} סותר את ההגדרה {% equation %}x=\sup B_{y}{% endequation %}. זה מסיים את החלק הזה של ההוכחה.

עכשיו צריך להוכיח ש-{% equation %}f\left(x+y\right)=f\left(x\right)+f\left(y\right){% endequation %}. כרגיל כבר, אנחנו מניחים שזה לא המצב ולכן אפשר לכתוב {% equation %}f\left(x+y\right)<f\left(x\right)+f\left(y\right){% endequation %} או {% equation %}f\left(x+y\right)>f\left(x\right)+f\left(y\right){% endequation %} ולהתעלל בכל אחד מהמקרים הללו לחוד עם כל מני רציונליים שנדחפים בין האיברים. במקרה {% equation %}f\left(x+y\right)<f\left(x\right)+f\left(y\right){% endequation %} אני אמצא {% equation %}p\in\mathbb{Q}_{1}{% endequation %} כך ש-{% equation %}f\left(x+y\right)<f\left(p\right)<f\left(x\right)+f\left(y\right){% endequation %} .

בואו נסתכל על {% equation %}f\left(x+y\right)<f\left(p\right){% endequation %}. בגלל ש-{% equation %}f{% endequation %} משמרת סדר, {% equation %}x+y<p{% endequation %}, ועכשיו נשתמש בטריק יפה. נמצא {% equation %}q_{x},q_{y}\in\mathbb{Q}_{1}{% endequation %} כך ש-{% equation %}p=q_{x}+q_{y}{% endequation %} ו-{% equation %}x<q_{x}{% endequation %} ו-{% equation %}y<q_{y}{% endequation %}, באופן הבא: מכיוון ש-{% equation %}x+y<p{% endequation %} אז {% equation %}x<p-y{% endequation %}, ולכן ניתן לבחור רציונלי {% equation %}q_{x}{% endequation %} כך ש-{% equation %}x<q_{x}<p-y{% endequation %}. עכשיו נגדיר {% equation %}q_{y}=p-q_{x}{% endequation %}; {% equation %}q_{y}{% endequation %} יהיה רציונלי כי {% equation %}p{% endequation %} ו-{% equation %}q_{x}{% endequation %} שניהם רציונליים. בנוסף, {% equation %}q_{y}=p-q_{x}>p-\left(p-y\right)=y{% endequation %}, כלומר קיבלתי {% equation %}x<q_{x}{% endequation %} וגם {% equation %}y<q_{y}{% endequation %}, כמו שרציתי.

עכשיו נשתמש במספרים הללו:

{% equation %}f\left(p\right)=f\left(q_{x}+q_{y}\right)=f\left(q_{x}\right)+f\left(q_{y}\right)>f\left(x\right)+f\left(y\right){% endequation %}

וקיבלנו סתירה ל-{% equation %}f\left(p\right)<f\left(x\right)+f\left(y\right){% endequation %}. המעבר השני מתבסס על כך ש-{% equation %}f{% endequation %} בגרסה המצומצמת שלה היא איזומורפיזם של {% equation %}\mathbb{Q}_{1}{% endequation %} ו-{% equation %}\mathbb{Q}_{2}{% endequation %}.

במקרה השני, {% equation %}f\left(x\right)+f\left(y\right)<f\left(x+y\right){% endequation %}, עושים משהו דומה - זה מה שנקרא "תרגיל טוב" כדי לוודא שהבנו את הרעיון.

נשאר לנו רק להראות {% equation %}f\left(x\cdot y\right)=f\left(x\right)\cdot f\left(y\right){% endequation %}. ראשית נוכיח את זה עבור ערכים חיוביים, {% equation %}0<x,y{% endequation %}, כי כאן נמצא עיקר הרעיון. כמו קודם, אני אניח שאין שוויון ואטפל במקרה {% equation %}f\left(xy\right)<f\left(x\right)f\left(y\right){% endequation %} והמקרה השני יהיה "תרגיל טוב". אני אמצא {% equation %}p\in\mathbb{Q}_{1}{% endequation %} כך ש-{% equation %}f\left(xy\right)<f\left(p\right)<f\left(x\right)f\left(y\right){% endequation %} ואז אמצא {% equation %}q_{x},q_{y}\in\mathbb{Q}_{1}{% endequation %} כך ש-{% equation %}x<q_{x},y<q_{y}{% endequation %} ו-{% equation %}q_{x}q_{y}=p{% endequation %} , כך שאני אקבל

{% equation %}f\left(p\right)=f\left(q_{x}q_{y}\right)=f\left(q_{x}\right)f\left(q_{y}\right)>f\left(x\right)f\left(y\right){% endequation %}

וזו סתירה ל-{% equation %}f\left(p\right)<f\left(x\right)f\left(y\right){% endequation %}.

נשאר רק למצוא את {% equation %}q_{x},q_{y}{% endequation %} הללו. {% equation %}xy<p{% endequation %} ולכן {% equation %}x<\frac{p}{y}{% endequation %} - אבל שימו לב שכאן נזקקתי להנחה ש-{% equation %}0<y{% endequation %} אחרת זה לא היה עובד (הנחה שלא הייתי צריך במקרה של חיבור, כשאמרתי ש-{% equation %}x<p-y{% endequation %}). עכשיו אפשר רציונלי {% equation %}q_{x}{% endequation %} כך ש-{% equation %}x<q_{x}<\frac{p}{y}{% endequation %} ואגדיר {% equation %}q_{y}=\frac{p}{q_{x}}{% endequation %} (ושוב, בלי {% equation %}0<x{% endequation %} הייתי מסתכן כאן בחלוקה באפס). עם ההגדרה הזו, {% equation %}q_{x}q_{y}=p{% endequation %} וכמו כן {% equation %}q_{y}{% endequation %} רציונלי כי הוא מנה של שני רציונליים. אנחנו יודעים ש-{% equation %}x<q_{x}{% endequation %} על פי האופן שבו {% equation %}q_{x}{% endequation %} נבחר. בנוסף, מכיוון ש-{% equation %}q_{x}<\frac{p}{y}{% endequation %} ושני המספרים הללו חיוביים, אנחנו מקבלים {% equation %}\frac{1}{q_{x}}>\frac{y}{p}{% endequation %} ולכן {% equation %}q_{y}=\frac{p}{q_{x}}>p\cdot\frac{y}{p}=y{% endequation %} וקיבלנו גם את {% equation %}q_{y}>y{% endequation %} שהיינו צריכים.

הראינו את {% equation %}f\left(xy\right)=f\left(x\right)f\left(y\right){% endequation %} למקרה שבו {% equation %}0<x,y{% endequation %}, אבל מה עם המקרים האחרים? ראשית, אם {% equation %}x=0{% endequation %} אז קל לראות ש-{% equation %}f\left(0\right)=0{% endequation %}, פשוט כי {% equation %}f\left(0\right)=f\left(0+0\right)=f\left(0\right)+f\left(0\right){% endequation %}, אז השוויון בוודאי יתקיים כי

{% equation %}f\left(xy\right)=f\left(0\cdot y\right)=f\left(0\right)=0=0\cdot f\left(y\right)=f\left(0\right)\cdot f\left(y\right)=f\left(x\right)f\left(y\right){% endequation %}

ובדומה גם אם {% equation %}y=0{% endequation %}. שימו לב שכאן לא השתמשנו במה שהוכחנו כבר על כפל, אבל כן במה שהוכחנו כבר על חיבור (טוב, ליתר דיוק רק על {% equation %}f\left(0+0\right)=f\left(0\right)+f\left(0\right){% endequation %} שנבע מכך ש-{% equation %}f{% endequation %} המקורית על הרציונליים הייתה איזומורפיזם).

עכשיו, מה אם {% equation %}x<0{% endequation %} אבל {% equation %}y>0{% endequation %}? במקרה הזה {% equation %}-x>0{% endequation %} אז אפשר להשתמש עליו במה שכבר הוכחנו. לפני כן, בואו נראה שמתקיים הדבר המתבקש {% equation %}f\left(-x\right)=-f\left(x\right){% endequation %}, מה שמזמין שוב שימוש במה שהוכחנו על חיבור:

{% equation %}f\left(-x\right)+f\left(x\right)=f\left(-x+x\right)=f\left(0\right)=0{% endequation %}

ולכן אחרי העברת אגפים נקבל {% equation %}f\left(-x\right)=-f\left(x\right){% endequation %}. ועכשיו אפשר לחזור אל הכפל:

{% equation %}f\left(xy\right)=-f\left(-xy\right)=-f\left(-x\right)f\left(y\right)=f\left(x\right)f\left(y\right){% endequation %}

ובאופן דומה מטפלים במקרה שבו {% equation %}x>0{% endequation %} ו-{% equation %}y<0{% endequation %}. ואם {% equation %}x,y<0{% endequation %} שניהם? זה הכי קל:

{% equation %}f\left(xy\right)=f\left(\left(-x\right)\left(-y\right)\right)=f\left(-x\right)f\left(-y\right)=\left(-1\right)^{2}f\left(x\right)f\left(y\right)=f\left(x\right)f\left(y\right){% endequation %}

וסיימנו את כל ההוכחה!

<h2>סיכום זריז</h2>

זה היה פוסט ארוך במיוחד ומחולק להרבה חלקים כי רציתי שכל הדברים הרלוונטיים זה לזה ישבו באותו מקום. יש משהו קצת אירוני שעבור ההגדרה המאוד פשוטה "הממשיים הם השדה הסדור השלם" הייתי צריך לכתוב כל כך הרבה, ועוד יותר אירוני שבעצם לא בנינו את הממשיים בכלל כאן. קיבלנו מושג מאוד ברור של מה הממשיים <strong>אמורים להיות</strong>: מה זה שדה, מה זה סדור, מה זה שלם. ראינו גם ש<strong>אם</strong> בכלל קיימת קבוצה שמקיימת את התכונות הללו שאנחנו דורשים מהממשיים, אז היא יחידה במובן זה שכל קבוצה אחרת שמקיימת את התכונות הללו איזומורפית אליה. אבל עדיין לא בניתי שום קבוצה כזו - את זה אני אעשה בהמשך, עם שתי הבניות הסטנדרטיות של הממשיים: זו שמשתמשת ב<strong>חתכי דדקינד</strong> וזו שמשתמשת ב<strong>סדרות קושי</strong>. ההגדרה של חתכי דדקינד מגיעה באופן כמעט ישיר מאקסיומת השלמות שדיברנו עליה בפוסט הזה; אבל ההגדרה עם סדרות קושי (שאני אישית אוהב טיפה יותר למרות ששתי ההגדרות נהדרות) תדרוש עוד קצת עבודת הכנה תיאורטית, שבה יעסוק הפוסט הבא. 
