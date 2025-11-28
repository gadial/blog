---
title: "מה בעצם הולך בטריגונומטריה בתיכון? (חלק א')"
layout: post
categories:
  - כללי
tags:
  - טריגונומטריה
social_media_share: true
---


<h2>מבוא</h2>

אני רוצה להתמודד עם אחת מטראומות המתמטיקה הגדולות שלי, אם לא הגדולה מכולן - טריגונומטריה תיכונית. ואני חושב שאין דבר שמעביר את גודל הטראומה טוב יותר מאשר צפייה בדף הנוסחאות לטריגונומטריה:

<img src="{{site.baseurl}}{{site.post_images}}/2021/trigo_formulas.png" alt=""/>


מה הולך כאן? ובכן, אנחנו מייד רואים שיש לנו עסק עם שני יצורים לא ברורים שנקראים {% equation %}\sin{% endequation %} ו-{% equation %}\cos{% endequation %} שעושים כל מני... דברים... שמערבים המון סימני פלוס ומינוס שנראים אקראיים לגמרי, ויש גם איזה "רדיאנים" שנכנסים לתמונה פה. עכשיו, תגידו, זו דרך לא הוגנת להציג טריגונומטריה! אחרי שלומדים את המושגים עצמם ומגיעים לפתרון תרגילים הכל מתבהר! ובכן, לא. היכרות עמוקה יותר עם החומר מתבטאת בהיכרות עם עוד נוסחאות מזעזעות במידה דומה, ועם תרגילים בסגנון "הוכיחו את הזהות {% equation %}\sin^{2}3\alpha-\sin^{2}\alpha=\sin2\alpha\sin4\alpha{% endequation %}".

מכאן קצרה הדרך לשאלה המצמיתה - <strong>בשביל מה צריך את זה</strong>. האם בחיי היומיום שלנו נוכיח זהויות טריגונומטריות? לא! אף פעם! ובכן, אולי אם נלך לאוניברסיטה ונלמד שם, נאמר, מתמטיקה ומדעי המחשב נזדקק לזה? ובכן, בקושי רב. ולרוב ברמה מאוד בסיסית. ובכן, אולי במקצועות מדעיים או הנדסיים אחרים צריך את זה ברמת אינטנסיביות גדולה יותר? ייתכן, אבל אז למה לא ללמוד את זה באופן ייעודי רק שם? אין תשובה טובה לשאלות הללו. <a href="https://gadial.net/2015/09/21/math_and_school/">כפי שכבר אמרתי בעבר</a>, אין לי תשובה טובה לשאלה מה צריך ללמד או לא ללמד בבית הספר כי זה נושא סבוך בהרבה מאשר סתם "בואו נעיף את כל מה שמעצבן אותנו". מבחינתי השאלה היא לא האם צריך ללמד את זה, אלא <strong>האם אפשר ללמד את זה ברור</strong>.

כאן, לדעתי, התשובה היא "כן". אני מקווה שלפחות בחלק מבתי הספר מלמדים את זה יותר ברור מאשר זה היה לי; אבל אני לא יודע מה עושים בכלל בתי הספר ולכן אנסה לכתוב כאילו קהל היעד שלי הוא גדי מחטיבת הביניים שלא הבין כלום ושנא הכל, ונראה אם אני אצליח לגרום לנודניק הזה עם גישת האנטי שלו לשנוא קצת פחות את החומר. או שבדרך אני אתחיל לשנוא את החומר עוד יותר.

בואו נתחיל.

<h2>מה זה בכלל סינוסים וקוסינוסים?</h2>

הכוכבות המרכזיות של הטריגו הן שתי פונקציות שנקראות "סינוס" ו"קוסינוס" ומסומנות בתור {% equation %}\sin x{% endequation %} ו-{% equation %}\cos x{% endequation %}. הכוונה ב"פונקציה" היא שלכל מספר {% equation %}x{% endequation %} שאני נותן להן כקלט, הן מחזירות מספר כפלט. במתמטיקה, הפונקציות הללו <strong>מאוד</strong> חשובות; הן מופיעות באופן טבעי בהקשרים רבים ושונים, שהמשותף לכולם על פי רוב הוא קיום של <strong>מחזוריות</strong> כלשהי. דוגמא מוכרת יחסית מחיי היום יום היא זו של אקוולייזר של מוזיקה:

<img src="{{site.baseurl}}{{site.post_images}}/2021/equalizer.png" alt=""/>

אקוולייזר יודע להחליש או להגביר תדירויות מסויימות של צליל, מה שמשפיע על האופן שבו אנחנו שומעים מוזיקה (למשל, אפשר "לחזק את הבאסים"). הרעיון מאחורי אקוולייזר הוא שצליל, גם כזה מורכב, הוא בעצם גל מחזורי, ואפשר לפרק את הגל המורכב הזה לסכום של גלים פשוטים יותר ולחזק/להחליש כל אחד מהגלים הפשוטים הללו באופן אינדיבידואלי. התיאור של הגלים הפשוטים יותר הללו מתבסס על סינוס וקוסינוס (הדוגמא הזו היא מקרה פרטי של מה שנקרא "טורי פורייה"; קסם מתמטי שמאפשר לתאר את רוב הדברים המחזוריים בתור סכום שכזה של סינוסים וקוסינוסים פשוטים).

עוד מקום שבו סינוסים וקוסינוסים צצים באופן טבעי הוא למשל במה שקורה כשאנחנו מותחים משהו שמחובר לקפיץ, משחררים אותו ומביטים בתנועה (המחזורית!) שלו. אפשר לכתוב משוואות שמתארות את התנועה; אלו יהיו משוואות מורכבות יחסית, שנקראות <strong>משוואות דיפרנציאליות</strong>, והפתרון שלהן יוצא בדיוק סינוסים וקוסינוסים - כלומר, התיאור של התנועה של המשהו-שמחובר-לקפיץ ייעזר בסינוסים וקוסינוסים. <a href="https://gadial.net/2010/03/31/sine_and_cosine_via_ode/">כשהצגתי בעבר</a> את הפונקציות הללו בבלוג, השתמשתי בגישה הזו.

העניין הוא שהדוגמאות הללו הן אולי מעניינות (אני מקווה) וחשובות אבל הן <strong>קשות</strong>. כשמגיעים ללמוד על טריגונומטריה בבית הספר עדיין אין את הרקע הנדרש כדי להיכנס לעובי הקורה הטכנית שלהן. בשל כך, האופן שבו מגדירים סינוסים וקוסינוסים הוא בעזרת <strong>משולש ישר זווית</strong> ועלול להתקבל רושם מוטעה שזו המהות היחידה של הפונקציות הללו. אז כאמור - זה לא כך, ואנחנו מתחילים ממשולשים פשוט כי זו הדרך הקלה ביותר עבורנו להגדיר באופן מדויק את הפונקציות הללו.

אז הרי לנו, משולש ישר זווית:

<img src="{{site.baseurl}}{{site.post_images}}/2021/rtriangle.png" alt=""/>

כדרכם של משולשים יש לו שלושה קודקודים {% equation %}A,B,C{% endequation %} שיוצרים שלוש צלעות {% equation %}AB,AC,BC{% endequation %} שהאורכים שלהן מתוארים עם {% equation %}a{% endequation %} (עבור {% equation %}BC{% endequation %}), עם {% equation %}b{% endequation %} (עבור {% equation %}AC{% endequation %}) ועם {% equation %}c{% endequation %} (עבור {% equation %}AB{% endequation %}). בנוסף יש למשולש שלוש <strong>זוויות</strong> (מה זו בעצם זווית? אני חושב עליה בתור "כמות סיבוב" אבל ההגדרה הטובה ביותר שאני מכיר היא - "נו, אתם יודעים").הזווית {% equation %}\angle BAC{% endequation %} שמסומנת באות היוונית {% equation %}\alpha{% endequation %}, הזווית {% equation %}\angle ABC{% endequation %} שמסומנת באות היוונית {% equation %}\beta{% endequation %}, והזווית {% equation %}\angle ACB{% endequation %} שלא מסומנת על ידי שום אות אלא על ידי ריבוע קטן כדי לציין שזו זווית <strong>ישרה</strong> - זווית בת {% equation %}90^{\circ}{% endequation %}, רבע סיבוב שלם.

כאן נדרש הסבר קטן על איך מודדים זוויות. בפוסט הזה אני משתמש בשיטת מדידה שנקראת <strong>מעלות</strong>. מעלות מוגדרות כך שסיבוב שלם הוא בן 360 מעלות, וכותבים את זה {% equation %}360^{\circ}{% endequation %}, כלומר עם עיגול קטן למעלה. למה 360? כי זה מספר נחמד שמתחלק בהמון דברים - יותר קליל להגיד "90 מעלות" במקום "{% equation %}\frac{1}{4}{% endequation %} סיבוב" ויותר קליל להגיד "60 מעלות" במקום {% equation %}\frac{1}{6}"{% endequation %} סיבוב" וכדומה. יש עוד שיטות מדידה לזווית, כשהחשובה והשימושית שבהן היא מדידה באמצעות <strong>רדיאנים</strong>. במדידה כזו, הזווית של סיבוב שלם היא בת {% equation %}2\pi{% endequation %} רדיאנים, כלומר מעלה אחת שווה ל-{% equation %}\frac{\pi}{180}{% endequation %} רדיאנים. <strong>למה</strong> רדיאנים זו שיטה חשובה ושימושית? יש לי פוסט על זה ואולי אגיע לנושא הזה גם פה, אבל כרגע בואו נשכח לגמרי מהשיטה הזו - אנחנו לא צריכים אותה, ולדעתי יותר נוח לדבר על מעלות מאשר על רדיאנים בשלב הזה.

על הצלעות במשולש אנחנו אומרים שהן נמצאות <strong>מול</strong> זוויות מסויימות. הצלע {% equation %}BC{% endequation %}, שאורכה היה {% equation %}a{% endequation %}, נמצאת מול הזווית {% equation %}\alpha{% endequation %}; הצלע {% equation %}AC{% endequation %} נמצאת מול {% equation %}\beta{% endequation %}; ואילו {% equation %}AB{% endequation %} נמצאת מול הזווית הישרה. במשולש ישר זווית שכזה קוראים בשם <strong>היתר</strong> לצלע שמול הזווית הישרה, ושתי הצלעות האחרות הן <strong>הניצבים</strong>. אלו הרבה שמות וסימונים אבל נזדקק להם בהמשך.

עכשיו, משולשים ישרי זווית יכולים להגיע בשלל צורות וגדלים, הנה עוד כמה לדוגמא:

<img src="{{site.baseurl}}{{site.post_images}}/2021/rtriangle2.png" alt=""/>

במשולשים הללו הזוויות שונות, וגם אורכי הצלעות שונים. הרעיון הבסיסי בסינוס וקוסינוס הוא שהם מאפשרים לתאר את הקשר בין הזוויות של משולש ישר זווית ובין האורכים של הצלעות שלו. אבל צריך להיזהר פה. בתור דוגמא, בואו ניקח את המשולש שראינו קודם ונשים לידו גרסה מוקטנת שלו:

<img src="{{site.baseurl}}{{site.post_images}}/2021/rtriangle3.png" alt=""/>


המשמעות של "גרסה מוקטנת" היא שאמנם הצלעות קטנות יותר, אבל <strong>הזוויות</strong> של שני המשולשים זהות. בגאומטריה קוראים לשני משולשים עם אותן זוויות <strong>משולשים דומים</strong> והתכונה המרכזית של משולשים דומים הוא ש<strong>היחס</strong> בין הצלעות המתאימות שלהם הוא קבוע. כלומר, שמתקיים {% equation %}\frac{x}{a}=\frac{y}{b}=\frac{z}{c}{% endequation %}.

בואו ניקח שניה את המשוואה {% equation %}\frac{x}{a}=\frac{z}{c}{% endequation %}. נכפיל אותה ב-{% equation %}a{% endequation %} ונחלק אותה ב-{% equation %}z{% endequation %} ונקבל {% equation %}\frac{x}{z}=\frac{a}{c}{% endequation %}. כלומר, מצד אחד <strong>האורך</strong> של הצלעות במשולשים הללו שונה, אבל <strong>היחס</strong> שבין הניצב {% equation %}BC{% endequation %} ובין היתר {% equation %}AB{% endequation %} הוא <strong>קבוע</strong>, בלי קשר לגודל של המשולש, כל עוד הזוויות הן אותן זויות. היחס הזה מסומן {% equation %}\sin\alpha{% endequation %}, מה שצריך לקרוא בתור "סינוס אלפא".

כלומר, ההגדרה היא זו: {% equation %}\sin\alpha=\frac{a}{c}{% endequation %} כאשר {% equation %}a{% endequation %} היא אורך הניצב שמול הזווית {% equation %}\alpha{% endequation %} במשולש ישר זווית <strong>כלשהו</strong> שבו יש את הזווית {% equation %}\alpha{% endequation %}, ואילו {% equation %}c{% endequation %} הוא אורך היתר של המשולש הזה. באופן דומה מגדירים את קוסינוס אלפא, בתור {% equation %}\cos\alpha=\frac{b}{c}{% endequation %}. כלומר: הסינוס מתקבל כאשר מחלקים את אורך הניצב ש<strong>מול</strong> הזווית ביתר; הקוסינוס מתקבל כאשר מחלקים את אורך הניצב ש<strong>ליד</strong> הזווית ביתר.

למה זו הגדרה מעניינת? ובכן, נניח שאני נכנס לתוך תותח ומשתגר לי לאוויר ובואו נתעלם לרגע מזוטות כמו כוח הכבידה כך שיוצא שאני טס לי בקו ישר. אחרי שעברתי מרחק של {% equation %}r{% endequation %} מטרים באוויר, אני שואל את עצמי שתי שאלות - מה הגובה שלי? ומה המרחק על פני הקרקע שעברתי, כלומר אם פתאום אני אפול בקו ישר לקרקע, איפה אני אמצא?

ובכן, התשובה לשאלה הזו היא - "תלוי בזווית שבה שיגרו אותך", ואנחנו יכולים להשתמש בסינוס וקוסינוס כדי להכניס את הזווית לתמונה באופן מדויק. אמרתי ש-{% equation %}\sin\alpha=\frac{a}{c}{% endequation %} ולכן אפשר לכפול ב-{% equation %}c{% endequation %} ולקבל {% equation %}a=c\cdot\sin\alpha{% endequation %} ובדומה {% equation %}b=c\cdot\cos\alpha{% endequation %}. ועבור הסיפור שלי, שבו המרחק שעברתי באוויר הוא {% equation %}r{% endequation %}, נקבל שאהיה בגובה {% equation %}r\sin\alpha{% endequation %} ובמרחק אופקי {% equation %}r\cos\alpha{% endequation %}.
<img src="{{site.baseurl}}{{site.post_images}}/2021/rtriangle4.png" alt=""/>

הסיטואציה הזו הייתה זו שבה הבנתי לראשונה את השימושיות של סינוסים וקוסינוסים בעצמי. כלומר, לא <strong>בדיוק</strong> הסיטואציה שבה משגרים אותי מתותח, אבל הסיטואציה שבה אני יודע את האורך {% equation %}r{% endequation %} של משהו ואני צריך לדעת לפרק אותו לרכיבים - רכיב של "גובה" ורכיב של "מרחק אופקי". זה היה כשניסיתי לכתוב קוד שמצייר <strong>מעגל</strong> שרדיוסו הוא {% equation %}r{% endequation %} והייתי צריך למצוא את קואורדינטות ה-{% equation %}x,y{% endequation %} של כל נקודה על המעגל. עוד אחזור לנקודה הזו בהמשך.

בואו ננסה להבין מה ההגדרה שהצגתי יודעת לספר לנו על סינוסים וקוסינוסים.

<ul> <li>הם מוגדרים רק לזוויות בין {% equation %}0^{\circ}{% endequation %} ו-{% equation %}90^{\circ}{% endequation %} ולא כולל את שני הקצוות הללו. הסיבה לכך היא שבמשולש סכום המעלות הוא {% equation %}180^{\circ}{% endequation %} ו-{% equation %}90^{\circ}{% endequation %} כבר ננגסו על ידי הזווית הישרה, אז {% equation %}\alpha+\beta=90^{\circ}{% endequation %}. האבחנה הזו כבר נותנת לנו תחושה לגבי הבעייתיות שבהגדרת סינוס וקוסינוס כך. באופן כללי אלו פונקציות שמוגדרות <strong>לכל</strong> קלט ולא רק לזוויות מאוד ספציפיות; כלומר, מה שאנחנו רואים עם המשולש הוא רק חלק מהסיפור המלא ועוד אציג את הסיפור המלא בהמשך.</li>


<li>אינטואטיבית, ככל ש-{% equation %}\alpha{% endequation %} מתקרבת אל {% equation %}0^{\circ}{% endequation %}, כלומר ככל שהיתר נעשה יותר ויותר שטוח, כך הגובה שנגיע אליו מתקרב ל-0 בעצמו. כלומר, האינטואיציה שלנו היא ש-{% equation %}\sin0^{\circ}=0{% endequation %}. עכשיו, כשהיתר יהיה שטוח לגמרי המרחק האופקי שלנו יהיה בדיוק {% equation %}r{% endequation %}; כלומר, כדי שזה ישחק יפה עם הנוסחה {% equation %}r\cos\alpha{% endequation %} שראינו עבור המרחק האופי, צריך שיתקיים {% equation %}\cos0^{\circ}=1{% endequation %}. שיקולים דומים יראו לנו שאינטואיטבי שיתקיים {% equation %}\sin90^{\circ}=1{% endequation %} ו-{% equation %}\cos90^{\circ}=0{% endequation %}. הסימטריה הזו בין סינוס וקוסינוס אינה מקרית ונרחיב עליה בהמשך.</li>


<li>אחת התכונות המפורסמות ביותר של משולש ישר זווית היא <strong>משפט פיתגורס</strong>: אם אורכי הניצבים במשולש ישר זווית הם {% equation %}a,b{% endequation %} והיתר הוא {% equation %}c{% endequation %} אז {% equation %}a^{2}+b^{2}=c^{2}{% endequation %}. כזכור, ראינו ש-{% equation %}a=c\sin\alpha{% endequation %} ו-{% equation %}b=c\cos\alpha{% endequation %} ולכן אם נציב את אלו במשוואה נקבל {% equation %}c^{2}\sin^{2}\alpha+c^{2}\cos^{2}\alpha=c^{2}{% endequation %}. אם נחלק ב-{% equation %}c^{2}{% endequation %} נקבל {% equation %}\sin^{2}\alpha+\cos^{2}\alpha=1{% endequation %}. הנוסחה הזו היא אחת מהנוסחאות הבסיסיות ביותר שקשורות לטריגונומטריה והייתי מצפה שתופיע בדף הנוסחאות שהבאתי למעלה - אבל היא לא! מה שכן, בדף נוסחאות לשלוש יחידות מתמטיקה מצאתי אותה, אבל רק באופן מובלע שכזה:</li>

</ul>
<img src="{{site.baseurl}}{{site.post_images}}/2021/trigo_formulas2.png" alt=""/>

דבר אחד שטרם התייחסתי אליו כלל הוא הזווית הנוספת במשולש שאינה ישרה - הזווית שקראתי לה {% equation %}\beta{% endequation %}:

<img src="{{site.baseurl}}{{site.post_images}}/2021/rtriangle.png" alt=""/>

העניין הוא ש-{% equation %}\beta{% endequation %} היא לא זווית עצמאית. כאמור, סכום הזוויות במשולש הוא {% equation %}180^{\circ}{% endequation %} ולכן {% equation %}\alpha+\beta+90^{\circ}=180^{\circ}{% endequation %}, כלומר {% equation %}\beta=90^{\circ}-\alpha{% endequation %}. עכשיו, הצלע שמול {% equation %}\beta{% endequation %} היא הצלע שאורכה {% equation %}b{% endequation %}, ולכן מאותה הגדרה של סינוס נקבל {% equation %}\sin\beta=\frac{b}{c}{% endequation %}. כזכור, הגדרנו גם {% equation %}\cos\alpha=\frac{b}{c}{% endequation %} כך שקיבלנו {% equation %}\sin\beta=\cos\alpha{% endequation %}, ואם נציב חזרה את הנוסחה שמצאנו: {% equation %}\cos\alpha=\sin\left(90^{\circ}-\alpha\right){% endequation %}.

באותו אופן, {% equation %}\cos\beta=\frac{a}{c}{% endequation %} יוביל אותנו אל הנוסחה {% equation %}\sin\alpha=\cos\left(90^{\circ}-\alpha\right){% endequation %}. בואו נכתוב אותן במפורש:

<ul> <li>{% equation %}\sin\alpha=\cos\left(90^{\circ}-\alpha\right){% endequation %}</li>


<li>{% equation %}\cos\alpha=\sin\left(90^{\circ}-\alpha\right){% endequation %}</li>

</ul>

מה הנוסחאות הללו אומרות? ובכן, שאפשר לחשוב על קוסינוס בתור סוג של "סינוס מורצת אחורה". כשאנחנו ב-{% equation %}\alpha=0{% endequation %} אז {% equation %}\cos\alpha{% endequation %} נמצאת באותו מקום שבו {% equation %}\sin90^{\circ}{% endequation %} נמצאת ואז כשמגדילים את {% equation %}\alpha{% endequation %} אפשר לראות ש-{% equation %}\cos\alpha{% endequation %} עושה מין הרצה ברברס של מה ש-{% equation %}\sin\alpha{% endequation %} עושה כשהיא מתקרבת אל {% equation %}90^{\circ}{% endequation %}. ככה זה נראה:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sin_graph1.png" alt=""/>

הסימטריה בין הפונקציות ברורה - הקו הצהוב שמייצג קוסינוס הוא תמונת ראי של הקו הצהוב שמייצג סינוס. אבל חייבים להודות ששתי הפונקציות לא נראות מרשימות או מעניינות במיוחד. הן סתם... קו כזה?

אז בואו נעבור להגדרה כללית יותר של סינוס וקוסינוס שמאפשרת לנו לתאר אותם לכל זווית אפשרית, לא רק בין {% equation %}0^{\circ}{% endequation %} ו-{% equation %}90^{\circ}{% endequation %}. אני כבר אגלה שמה שיתגלה הוא שה"סתם קו כזה" הוא בעצם כל מה שיש - כל מה שנראה בהמשך הוא כל מני הזזות ושיקופים נוספים של הקו הזה, כך שיוצא שהוא בעצם אחד מהקווים החשובים במתמטיקה.

<h2>איך מגדירים באופן כללי סינוסים וקוסינוסים?</h2>

אני ארצה להגדיר סינוס וקוסינוס באופן כללי בעזרת <strong>מעגל היחידה</strong>, שזה השם המפוצץ שנותנים למעגל שהרדיוס שלו הוא מאורך 1 (זו ה"יחידה") והמרכז שלו הוא <strong>ראשית הצירים</strong>, כלומר נקודה שהקואורדינטות שלה הן {% equation %}0,0{% endequation %}:

<img src="{{site.baseurl}}{{site.post_images}}/2021/unit_circle.png" alt=""/>

ה"צירים" המדוברים הם הקווים המאונכים שנפגשים במרכז המעגל. לקו האופקי קוראים "ציר {% equation %}x{% endequation %}" ולאנכי "ציר {% equation %}y{% endequation %}". 

עכשיו, בואו ניקח רדיוס כלשהו של המעגל - כלומר, קו ישר ממרכז המעגל אל המעגל עצמו (ב"המעגל" אני מתכוון רק לשפה של העיגול האפור):

<img src="{{site.baseurl}}{{site.post_images}}/2021/unit_circle2.png" alt=""/>

אני מסמן ב-{% equation %}\left(b,a\right){% endequation %} את הקואורדינטות של הנקודה על המעגל שאליה הרדיוס מגיע (למה לא {% equation %}\left(a,b\right){% endequation %}? תכף נראה), וב-{% equation %}\alpha{% endequation %} את הזווית שהרדיוס הזה יוצר עם הקו האופקי של ציר {% equation %}x{% endequation %} - ליתר דיוק, עם מה שנקרא <strong>הכיוון החיובי</strong> של ציר {% equation %}x{% endequation %}, שבאיור שלי (ובכל יתר האיורים במתמטיקה, כי זו המוסכמה המקובלת...) פונה לכיוון צד ימין.

עכשיו אפשר להגדיר סינוסים וקוסינוסים באופן כללי:

<ul> <li>{% equation %}\sin\alpha=a{% endequation %}</li>


<li>{% equation %}\cos\alpha=b{% endequation %}</li>

</ul>

אבל רגע, מה זה בעצם קואורדינטות? ובכן, לכל נקודה במישור יש קואורדינטה {% equation %}\left(b,a\right){% endequation %} שאומרת כמה צריך לזוז בכיוון ימינה/שמאלה (זה {% equation %}b{% endequation %}) וכמה צריך לזוז בכיוון למעלה/למטה (זה {% equation %}a{% endequation %}) כדי להגיע אל הנקודה. כדי לראות את זה אוסיף עוד קווים לאיור:

<img src="{{site.baseurl}}{{site.post_images}}/2021/unit_circle3.png" alt=""/>

הקו הירוק המקווקו הוא מה שצריך ללכת "למעלה" כדי להגיע אל הנקודה, אם אנחנו נמצאים על ציר {% equation %}x{% endequation %}. הקו הסגול הוא כמה צריך ללכת "ימינה". האורך של הקו הירוק הוא {% equation %}a{% endequation %} והאורך של הקו הסגול הוא {% equation %}b{% endequation %}. שימו לב שהקו הסגול והירוק, יחד עם החלקים המתאימים מצירים {% equation %}x,y{% endequation %}, מייצרים מלבן; צלעות נגדיות במלבן הן שוות בגודלן, אז אפשר לסמן ב-{% equation %}b{% endequation %} גם את החלק מציר {% equation %}x{% endequation %} למטה שמתחיל בראשית הצירים ומסתיים בתחילת הקו הירוק. ועכשיו, מה קיבלנו? בדיוק את המשולש ישר הזווית שעבורו הגדרנו סינוס וקוסינוס קודם; אנחנו רואים שבמקרה הזה, ההגדרה ה"חדשה" אכן מכלילה את ההגדרה הקודמת.

אבל נו, מה הרווחנו מכל הסיבוך הזה אם בסך הכל קיבלתי את ההגדרה הקודמת? ובכן, בואו ניקח את זה צעד אחד קדימה ניקח את הרדיוס שלנו ונסובב אותו קצת נגד כיוון השעון עד אשר יגיע אל הרביע השמאלי-עליון של המעגל:

<img src="{{site.baseurl}}{{site.post_images}}/2021/unit_circle4.png" alt=""/>

מה קורה פה? לכאורה הגעתי למשהו שנראה כמו תמונת ראי של הסיטואציה הקודמת וציירתי משולש גם בה, אבל שימו לב שהזווית בתוך המשולש, שאני מסמן ב-{% equation %}\beta{% endequation %}, <strong>אינה</strong> הזווית שמעניינת אותנו כאן אלא הזווית ה"מתוחה" שאני מסמן ב-{% equation %}\alpha{% endequation %}. זכרו את ההגדרה שנתתי: אני לוקח את הזווית שנוצרת בין הרדיוס ובין <strong>הכיוון החיובי</strong> של ציר {% equation %}x{% endequation %}. כלומר, את כמות הסיבוב שנדרשת כדי להביא את הרדיוס למקומו הנוכחי, אם הוא מתחיל כשהוא מונח על הכיוון החיובי של ציר {% equation %}x{% endequation %} ומתחיל להסתובב נגד כיוון השעון.

אם כן, גם בתמונה הזו {% equation %}\sin\alpha=a{% endequation %} ו-{% equation %}\cos\alpha=b{% endequation %}, ואנחנו רואים איך ההגדרה שלנו מטפלת גם במקרים שלא נופלים בין {% equation %}0^{\circ}{% endequation %} ו-{% equation %}90^{\circ}{% endequation %}. אבל למעשה, אנחנו רואים יותר מכך. מכיוון שהזוויות {% equation %}\alpha,\beta{% endequation %} ביחד מייצגות בדיוק חצי סיבוב (כמות הסיבוב שנדרשת כדי להביא את הרדיוס מהכיוון <strong>החיובי</strong> של ציר {% equation %}x{% endequation %} אל הכיוון <strong>השלילי </strong>שלו) הרי ש-{% equation %}\alpha+\beta=180^{\circ}{% endequation %}. עכשיו, אם מסתכלים על המשולש ישר הזווית ומשתמשים בהגדרה הקודמת שלנו של סינוס וקוסינוס, מקבלים ש-{% equation %}\sin\beta=a{% endequation %} ולכן קיבלנו את המשוואה

<ul> <li>{% equation %}\sin\left(180^{\circ}-\alpha\right)=\sin\alpha{% endequation %}</li>

</ul>

זו משוואה שמספרת לנו על סימטריה של הפונקציה {% equation %}\sin{% endequation %} עצמה, ביחס לנקודה של {% equation %}90^{\circ}{% endequation %}. כלומר, שמתקיים {% equation %}\sin\left(90^{\circ}+x\right)=\sin\left(90^{\circ}-x\right){% endequation %}. למה זה נכון? ובכן, אם נסמן {% equation %}\alpha=90^{\circ}+x{% endequation %} אז {% equation %}\sin\left(90^{\circ}+x\right)=\sin\alpha=\sin\left(180^{\circ}-\alpha\right)=\sin\left(90^{\circ}-x\right){% endequation %}. עכשיו, ראינו קודם ש-{% equation %}\sin\left(90^{\circ}-x\right)=\cos x{% endequation %}, כלומר קיבלנו ש-{% equation %}\sin\left(90^{\circ}+x\right)=\cos x{% endequation %}, ובמילים אחרות - אחרי שסינוס מגיעה אל קו ה-90 מעלות היא מתחילה להתנהג כמו קוסינוס. בהמשך נראה שזה כך באופן כללי - קוסינוס הוא בעצם סינוס עם "הזזה" של {% equation %}90^{\circ}{% endequation %} קדימה בזמן. תכף נראה איך כל זה מתבטא בגרף של {% equation %}\sin{% endequation %}, אבל קודם כל בואו נראה מה קורה עם קוסינוס. וזה יהיה קצת יותר טריקי.

מפתה לומר ש-{% equation %}\cos\beta=b{% endequation %} כי זה מתאים למה שראינו קודם, אבל זה פשוט לא נכון, מהטעם הפשוט ש-{% equation %}b{% endequation %} כאן הוא מספר <strong>שלילי</strong>, אבל ההגדרה הקודמת שלנו של קוסינוס, שהתבססה על משולש ובה אנחנו מנסים להשתמש עבור {% equation %}\cos\beta{% endequation %}, דיברה על <strong>האורך</strong> של הצלעות. האורך של הצלע שליד {% equation %}\beta{% endequation %} הוא לא {% equation %}b{% endequation %}; הוא {% equation %}\left|b\right|{% endequation %} ומכיוון ש-{% equation %}b{% endequation %} שלילי אפשר גם לומר שהוא {% equation %}-b{% endequation %}. כלומר, אנחנו מקבלים

<ul> <li>{% equation %}\cos\left(180^{\circ}-\alpha\right)=-\cos\alpha{% endequation %}</li>


<li>זה הופך את קוסינוס לפונקציה <strong>אנטי-סימטרית</strong> ביחס לנקודה {% equation %}90^{\circ}{% endequation %}, כלומר {% equation %}\cos\left(90^{\circ}+x\right)=-\cos\left(90^{\circ}-x\right)=-\sin x{% endequation %}. בואו נראה איך זה נראה בגרפים:</li>

</ul>

<img src="{{site.baseurl}}{{site.post_images}}/2021/sin_graph2.png" alt=""/>

העברתי קו מקווקו אדום בדיוק ב-{% equation %}90^{\circ}{% endequation %} ואפשר לראות איך הקו הכחול סימטרי ביחס אליו (כלומר, כל צד נראה כמו תמונת ראי של השני) בעוד הקו הצהוב אנטי-סימטרי (כלומר, כל צד נראה כמו תמונת ראי ששוקפה עוד פעם, הפעם ביחס לציר {% equation %}x{% endequation %}, של השני), אבל יותר מעניין עכשיו הדמיון בין הקווים עצמם. שימו לב לאופן שבו הקו הכחול, של הסינוס, יורד בין {% equation %}90^{\circ}{% endequation %} ל-{% equation %}180^{\circ}{% endequation %}; לכו שמאלה לחלק שבין {% equation %}0^{\circ}{% endequation %} ו-{% equation %}90^{\circ}{% endequation %} ותראו שהקו הצהוב (של קוסינוס) נראה אותו דבר בדיוק. לעומת זאת לקו הצהוב של הקוסינוס היורד בין {% equation %}90^{\circ}{% endequation %} ו-{% equation %}180^{\circ}{% endequation %} עדיין אין מקבילה מדויק, אבל הוא בבירור נראה כמו <strong>שיקוף</strong> של הקו הכחול שבין {% equation %}0^{\circ}{% endequation %} ו-{% equation %}90^{\circ}{% endequation %}- שיקוף ביחס לציר {% equation %}x{% endequation %} (שלא ציירתי כאן במפורש; הקו האופקי שעובר דרך {% equation %}y=0{% endequation %}).

השלב הבא הוא להבין איך נראות הפונקציות {% equation %}\sin\left(180^{\circ}+x\right){% endequation %} ו-{% equation %}\cos\left(180^{\circ}+x\right){% endequation %} עבור ערכי {% equation %}x{% endequation %} מ-{% equation %}0^{\circ}{% endequation %} עד {% equation %}90^{\circ}{% endequation %}. בשביל זה נמשיך לסובב את הרדיוס שלנו עד שיגיע אל הרביע השלישי, השמאלי-תחתון:

<img src="{{site.baseurl}}{{site.post_images}}/2021/unit_circle5.png" alt=""/>

עכשיו אפשר לראות ש-{% equation %}\alpha{% endequation %} מורכבת מזווית של {% equation %}180^{\circ}{% endequation %} ועוד קצת, כשהקצת מתאר את הסיבוב ברביע השלישי והוא הזווית שמול {% equation %}a{% endequation %} במשולש שציירתי. במילים אחרות, אם {% equation %}\alpha=180^{\circ}+x{% endequation %} אנחנו רואים שמתקיים

{% equation %}\sin\left(180^{\circ}+x\right)=-\sin x{% endequation %}

{% equation %}\cos\left(180^{\circ}+x\right)=-\cos x{% endequation %}

כאשר המינוס בשני המקרים נובע ממה שהסברתי קודם - ערכי הנקודה {% equation %}\left(b,a\right){% endequation %} שניהם שליליים, אבל {% equation %}\sin x,\cos x{% endequation %} שווים ל<strong>אורך</strong> של הקטעים המתאימים במשולש, כלומר לערכים המוחלטים של {% equation %}a,b{% endequation %}.

אם נצייר את הגרף שמתקבל, זה מה שנראה:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sin_graph3.png" alt=""/>

כאן הקו הירוק (הקו המקווקו הימני) מתאר את תחילת החלק שדיברתי עליו. אם מסתכלים על העקום הכחול, של סינוס, רואים שהוא מתחיל את החלק הזה בגובה 0, בדיוק כמו שסינוס התחיל ב-{% equation %}0^{\circ}{% endequation %}, אבל בעוד שהסינוס של {% equation %}0^{\circ}{% endequation %} עולה למעלה עד 1, הסינוס של {% equation %}180^{\circ}{% endequation %} יורד למטה, עד {% equation %}-1{% endequation %}, כפי שתיארתי. דבר דומה קורה עם הקוסינוס, רק שהוא עולה כי הקוסינוס של {% equation %}0^{\circ}{% endequation %} היה בירידה.

כמעט סיימנו! כדי להבין את סינוס וקוסינוס עד הסוף צריך ללוות את הרדיוס שלנו רק עד הרביע האחרון, התחתון-ימני:

<img src="{{site.baseurl}}{{site.post_images}}/2021/unit_circle6.png" alt=""/>

כאן הזווית {% equation %}\alpha{% endequation %} התפתלה כל כך הרבה שהיא כבר נראית כמו פקמן. הפעם הזווית הפנימית בתוך המשולש היא מה שנדרש כדי להשלים סיבוב מלא של {% equation %}360^{\circ}{% endequation %} יחד עם {% equation %}\alpha{% endequation %}, כלומר היא שווה ל-{% equation %}360^{\circ}-\alpha{% endequation %}. כמו כן הפעם {% equation %}b{% endequation %} הוא חיובי ורק {% equation %}a{% endequation %} שלילי. לכן נקבל:

<ul> <li>{% equation %}\sin\left(360^{\circ}-\alpha\right)=-\sin\alpha{% endequation %}</li>


<li>{% equation %}\cos\left(360^{\circ}-\alpha\right)=\cos\alpha{% endequation %}</li>

</ul>

אם נציב {% equation %}\alpha=270^{\circ}+x{% endequation %}, נקבל ש-{% equation %}360^{\circ}-\alpha=90^{\circ}-x{% endequation %} ומכאן:

{% equation %}\sin\left(270^{\circ}+x\right)=-\sin\left(90^{\circ}-x\right)=-\cos x{% endequation %}

{% equation %}\cos\left(270^{\circ}+x\right)=\cos\left(90^{\circ}-x\right)=\sin x{% endequation %}

כלומר, החלק הזה של הסינוס מתנהג כמו שקוסינוס התנהג בין {% equation %}0^{\circ}{% endequation %} ו-{% equation %}90^{\circ}{% endequation %}, רק עולה במקום לרדת, בעוד שהקוסינוס עולה בדיוק כמו שסינוס עלה בין {% equation %}0^{\circ}{% endequation %} ו-{% equation %}90^{\circ}{% endequation %}:

<img src="{{site.baseurl}}{{site.post_images}}/2021/sin_graph4.png" alt=""/>

בגרף הזה כבר קל לראות בעיניים את האופן שבו הקו הכחול של הסינוס נראה <strong>בדיוק אותו דבר</strong> כמו הקו הצהוב של הקוסינוס, למעט זה שהקו של הקוסינוס מקדים אותו ב-{% equation %}90^{\circ}{% endequation %} - כלומר, אם ניקח את הקו הצהוב ונזיז את כולו {% equation %}90^{\circ}{% endequation %} ימינה, נקבל בדיוק את הקו הכחול.

עוד דבר שאפשר לראות בגרף הוא שכל הקווים שמופיעים בו הם בעצם הקו של סינוס מהקטע בין {% equation %}0^{\circ}{% endequation %} ו-{% equation %}90^{\circ}{% endequation %} - רק כשלוקחים את הקו הזה, משקפים אותו ומזיזים אותו. אני מקווה שעכשיו זה לא כזה מפתיע, פשוט כי ראינו שסינוס וקוסינוס הוגדרו שניהם בעזרת תנועה על מעגל היחידה, ומעגל היחידה הוא <strong>סימטרי</strong>. כל רביע שלו נראה בדיוק אותו דבר עד כדי שיקופים וסיבובים, לכן הגיוני שהפונקציות "יתנהגו דומה".

הנקודה האחרונה, והקריטית ביותר לענייננו, היא שסינוס וקוסינוס מסיימים את הגרף הזה, עם ההגעה ל-{% equation %}360^{\circ}{% endequation %}, בדיוק במקום שבו הם התחילו כשהיו ב-{% equation %}0^{\circ}{% endequation %}: סינוס ב-0 וקוסינוס ב-1. זה כמובן לא מקרי - אחרי שסיימנו להשלים סיבוב שלם סביב מעגל היחידה, חזרנו אל נקודת ההתחלה. אבל זה גם אומר שהפונקציות הללו הן <strong>מחזוריות</strong>: אם נרצה להפעיל אותן על זווית גדולה מ-{% equation %}360^{\circ}{% endequation %}, האפקט יהיה בדיוק של "נסובב את הרדיוס שלנו כמה סיבובים שלמים ואז את מה שנשאר". למשל, {% equation %}\sin400^{\circ}=\sin\left(360^{\circ}+40^{\circ}\right)=\sin40^{\circ}{% endequation %}. באופן כללי נקבל:

{% equation %}\sin\left(k\cdot360^{\circ}+\alpha\right)=\sin\alpha{% endequation %}

{% equation %}\cos\left(k\cdot360^{\circ}+\alpha\right)=\cos\alpha{% endequation %}

וזאת <strong>לכל</strong> מספר שלם {% equation %}k{% endequation %}. כולל שליליים, כי אפשר לחשוב על זווית שלילית פשוט בתור סיבוב של הרדיוס <strong>עם כיוון השעון</strong> במקום נגדו. ככה זה הולך להיראות (השארתי את הקווים המקווקווים כדי שנקבל תחושה של איפה כל מה שדיברנו עליו עד כה נמצא ביחס לתמונה הגדולה):

<img src="{{site.baseurl}}{{site.post_images}}/2021/sin_graph5.png" alt=""/>

כאן המחזוריות של הפונקציות, כמו גם העובדה שקוסינוס זה "סינוס מוזז קצת", כבר ברורה מאוד לעין, ואני מקווה שגם ברור מה קורה בחלקים האינדיבידואליים של הפונקציות. זה סוגר את השאלה הבסיסית של "מה אלו הפונקציות הללו בכלל?" אבל הסיפור רק מתחיל כאן - עדיין אין לי הסבר לכל הנוסחאות המפחידות שאיתן פתחתי. לכך נגיע בפעם הבאה. 