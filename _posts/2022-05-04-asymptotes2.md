---
title: "אסימפטוטות, חלק ב': הדברים שמתקרבים להיות קשים ואולי גם מגיעים לשם"
layout: post
categories:
  - אנליזה מתמטית
tags:
  - אסימפטוטה
description: 'מה קורה עם אסימפטוטות של פונקציות יותר מסובכות מסתם שברים, ומה ההגדרות הפורמליות?'
image: "2022/sqrt_complicated.png"
---


<h2>מבוא ותזכורת</h2>

<a href="https://gadial.net/2022/04/27/asymptotes/">בפוסט הקודם</a> דיברתי על מה זו אסימפטוטה של פונקציה. אינטואיטיבית זה קו ישר כלשהו שהפונקציה מתקרבת אליו עוד ועוד כשהגרף שלה "הולך לאינסוף". בפוסט הזה גם אציג את ההגדרה הפורמלית והלא אינטואיטיבית, אבל אשמור את זה לסוף - בינתיים אני רוצה לראות עוד פונקציות קונקרטיות והאסימפטוטות האפשריות שלהן. כזכור, בפוסט הקודם דיברתי על שני סוגים של פונקציות: <strong>פולינומים</strong> ו<strong>פונקציות רציונליות</strong>.

<strong>פולינום</strong> היה פונקציה מהצורה {% equation %}p\left(x\right)=a_{n}x^{n}+\ldots+a_{1}x+a_{0}{% endequation %} כאשר {% equation %}n{% endequation %} הוא מספר טבעי כלשהו שנקרא <strong>מעלת הפולינום</strong> ו-{% equation %}a_{n}\ne0{% endequation %} הוא מספר שנקרא <strong>המקדם המוביל</strong> של הפולינום. עבור פולינומים ראינו שפשוט אין להם אסימפטוטות; זה היה מקרה<strong> פשוט מדי</strong>.

השלב הבא היה <strong>פונקציות רציונליות</strong> שהן פונקציות מהצורה {% equation %}f\left(x\right)=\frac{p\left(x\right)}{q\left(x\right)}{% endequation %} כאשר {% equation %}p,q{% endequation %} שניהם פולינומים. למשל {% equation %}\frac{1}{x}{% endequation %} שהייתה דוגמת האב טיפוס שלי ל"פונקציה עם אסימפטוטות". עבור פונקציות כאלו ראינו שני דברים:

<ol> <li>האסימפטוטות <strong>האנכיות</strong> (אסימפטוטות שהן קו אנכי, למעלה-למטה) היו הקווים מהצורה {% equation %}x=a{% endequation %} כאשר {% equation %}a{% endequation %} היה <strong>שורש</strong> של {% equation %}q\left(x\right){% endequation %} (משהו שמאפס את הפולינום {% equation %}q\left(x\right){% endequation %} שבמכנה). זה לא עבד לכל שורש; רק לכאלו שלא איפסו את {% equation %}p\left(x\right){% endequation %}. עבור כאלו שאיפסו גם את המונה וגם את המכנה היה צורך לחלק ב-{% equation %}x-a{% endequation %} ולבדוק שוב.</li>


<li>האסימפטוטות <strong>האופקיות</strong> (אסימפטוטות שהן קו אופקי, ימינה-שמאלה) היו זהות גם כשהפונקציה הלכה לאינסוף וגם כשהלכה למינוס אינסוף, כלומר הייתה רק אסימפטוטה אופקית אחת לכל היותר. אם {% equation %}q\left(x\right){% endequation %} היה ממעלה גדולה מ-{% equation %}p\left(x\right){% endequation %}, האסימפטוטה הזו הייתה {% equation %}y=0{% endequation %}; אם {% equation %}p\left(x\right){% endequation %} היה ממעלה גדולה מ-{% equation %}q\left(x\right){% endequation %} לא היו אסימפטוטות (הפונקציה {% equation %}f\left(x\right){% endequation %} פשוט "בורחת" לאינסוף/מינוס אינסוף כש-{% equation %}x{% endequation %} הולך לשם), ואם הם היו ממעלה שווה אז האסימפטוטה הייתה {% equation %}y=\frac{a_{n}}{b_{n}}{% endequation %} כאשר {% equation %}a_{n}{% endequation %} המקדם המוביל של {% equation %}p\left(x\right){% endequation %} ו-{% equation %}b_{n}{% endequation %} המקדם המוביל של {% equation %}q\left(x\right){% endequation %}.</li>

</ol>

אפשר לחשוב על המקרה של פולינומים בתור מקרה פשוט למדי של פונקציות רציונליות: במקום לדבר על פולינום {% equation %}p\left(x\right){% endequation %} אפשר לדבר על הפונקציה הרציונלית {% equation %}\frac{p\left(x\right)}{q\left(x\right)}{% endequation %} כאשר {% equation %}q\left(x\right)=1{% endequation %} - פולינום קבוע ממעלה 0. מקרה 1 לא יכול להתקיים פה כי אין ערך שאפשר להציב ב-{% equation %}q\left(x\right){% endequation %} ולקבל 0, ומקרה 2 נופל תחת "{% equation %}p\left(x\right){% endequation %} ממעלה גדולה מ-{% equation %}q\left(x\right){% endequation %} (כי מעלת {% equation %}q\left(x\right)=0{% endequation %}) למעט המקרה שבו גם {% equation %}p\left(x\right){% endequation %} הוא קבוע ואז הפונקציה עצמה היא קו אופקי, ולכן מהווה את האסימפטוטה של עצמה (זה מקרה טריוויאלי כל כך שלא טרחתי להתייחס אליו קודם; בדרך כלל לא בודקים אסימפטוטות של קווים ישרים).

יופי. עכשיו, מה קורה עם פונקציות מסובכות אחרות, שאינן פונקציות רציונליות?

<h2>אסימפטוטות שמערבות שורשים</h2>

נתחיל עם פונקציה פשוטה יחסית - פונקציית ה<strong>שורש ריבועי</strong>. שורש ריבועי של מספר {% equation %}x{% endequation %} הוא מספר אי שלילי {% equation %}a{% endequation %} כך ש-{% equation %}a^{2}=x{% endequation %}; מסמנים זאת {% equation %}a=\sqrt{x}{% endequation %}. יש כאן שתי נקודות שצריך לשם לב אליהן:

<ol> <li>אם {% equation %}x{% endequation %} שלילי, <strong>אין לו שורש ריבועי</strong>. אין מספר ממשי {% equation %}a{% endequation %} כך ש-{% equation %}a^{2}=-1{% endequation %}, כי במספרים ממשיים כל מספר כפול עצמו יוצא אי-שלילי. השימוש שלי במילה "ממשיים" מרמז שיש סוג <strong>אחר</strong> של מספרים, <strong>מספרים מרוכבים</strong>, שבהם הסיטואציה מורכבת יותר ויש שורשים גם למספרים שליליים, אלא שאני לא אדבר עליהם כאן; הניתוח של פונקציות מרוכבות הוא משמעותית יותר מסובך ממה שנעשה כאן. לכן מבחינתנו, אם מה שבתוך השורש הוא שלילי, השורש פשוט לא מוגדר.</li>


<li>למספרים חיוביים יש למעשה <strong>שני</strong> שורשים ריבועים. למשל {% equation %}2^{2}=4{% endequation %} אבל גם {% equation %}\left(-2\right)^{2}=4{% endequation %}. גם באופן כללי - אם {% equation %}a^{2}=x{% endequation %} אז גם {% equation %}\left(-a\right)^{2}=x{% endequation %}. בגלל שהשורשים תמיד באים בזוגות כאלו של מספר/מינוס שלו, הקונבנציה שאנחנו עובדים איתה היא שכשמוציאים שורש למספר, כלומר כותבים {% equation %}a=\sqrt{x}{% endequation %}, אז {% equation %}a{% endequation %} תמיד יהיה השורש <strong>האי-שלילי</strong>. לפעמים, כשרוצים לדבר על שני השורשים יחד, משתמשים בסימון {% equation %}\pm{% endequation %}. כך למשל בנוסחת השורשים לפתרון משוואה ריבועית מהצורה {% equation %}ax^{2}+bx+c{% endequation %}: הנוסחה היא {% equation %}x_{1,2}=\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}{% endequation %}, וכאן מתייחסים לשני השורשים האפשריים של {% equation %}b^{2}-4ac{% endequation %}.</li>

</ol>

תמונה אחת כידוע שווה אלף מילים - חזרתי על זה שוב ושוב בפוסט הקודם. אז הנה תמונה של {% equation %}f\left(x\right)=\sqrt{x}{% endequation %}:

<img src="{{site.baseurl}}{{site.post_images}}/2022/sqrt_x.png" alt=""/>

והתמונה הזו... שווה מעט מאוד! כמעט כלום! אנחנו רואים ש-{% equation %}f\left(x\right){% endequation %} נקטעת בפתאומיות ב-{% equation %}x=0{% endequation %} (כי כאמור, היא לא מוגדרת לערכים קטנים יותר) אבל אין לה שם אסימפטוטה (הפונקציה לא בורחת לאינסוף), ובאשר למה שקורה כש-{% equation %}x\to\infty{% endequation %}? אי אפשר להבין כלום מהאיור. נראה שהפונקציה עולה, אבל בצורה "מתמתנת" שכזו (השם הפורמלי הוא <strong>פונקציה קעורה</strong>, אבל זה לא חשוב). אז מה קורה? התשובה היא ש-{% equation %}f\left(x\right)\underset{x\to\infty}{\to}\infty{% endequation %} ואפשר לראות את זה יחסית בקלות: נניח ש-{% equation %}y=a{% endequation %} זו אסימפטוטה של הפונקציה עם {% equation %}a\ge0{% endequation %} (עבור {% equation %}a<0{% endequation %} ברור שזו לא תהיה אסימפטוטה - הפונקציה לא מתקרבת לשם בכלל), ונסתכל על {% equation %}x=\left(a+1\right)^{2}{% endequation %}. אז {% equation %}f\left(x\right)=\sqrt{\left(a+1\right)^{2}}=a+1{% endequation %}. כלומר, מתישהו {% equation %}f\left(x\right){% endequation %} כבר בגובה {% equation %}1{% endequation %} מעל הקו {% equation %}y=a{% endequation %} ובהמשך היא רק תמשיך לעלות עוד ועוד, אז הקו הזה הוא לא אסימפטוטה.

האמת היא ש-{% equation %}\sqrt{x}{% endequation %} לא כל כך שונה מפולינומים בהיבט שמעניין אותנו. הנה דרך טובה להכניס אותו למשחק: אני מניח שאנחנו כבר מכירים את <strong>חוקי החזקות</strong>, שאומרים ש-{% equation %}x^{a}\cdot x^{b}=x^{a+b}{% endequation %} וגם ש-{% equation %}\left(x^{a}\right)^{b}=x^{ab}{% endequation %}. בהתחלה, החוקים הללו מוגדרים רק עבור חזקות שהן מספרים טבעיים, אבל אם מניחים לרגע שהן מוגדרות גם עבור שברים, אז מייד רואים שצריך להתקיים {% equation %}x^{\frac{1}{2}}\cdot x^{\frac{1}{2}}=x^{1}=x{% endequation %}. כלומר, אם יש משמעות לביטוי {% equation %}x^{\frac{1}{2}}{% endequation %} ואנחנו חושבים עליו בתור מספר {% equation %}a=x^{\frac{1}{2}}{% endequation %}, אז בפרט צריך להתקיים {% equation %}a^{2}=x{% endequation %}, כלומר {% equation %}a{% endequation %} הוא אחד מהשורשים של {% equation %}x{% endequation %}. זה מוביל אותנו ל<strong>הגדרה</strong> {% equation %}x^{\frac{1}{2}}=\sqrt{x}{% endequation %}, וזו הגדרה מועילה למדי כי החוקים שראינו קודם על פונקציות רציונליות ופולינומים עובדות גם עבור {% equation %}x{% endequation %} בחזקה שהיא שבר.

אל מה אני מתכוון? ובכן, במקום לדבר על {% equation %}f\left(x\right)=\sqrt{x}{% endequation %} אפשר לדבר על הפונקציה הרציונלית {% equation %}f\left(x\right)=\frac{x^{\frac{1}{2}}}{1}{% endequation %}, והחוקים שראינו קודם עבור פונקציות רציונליות תקפים גם כאן ומראים לנו מייד שאין אסימפטוטה (כי המעלה של המונה, {% equation %}\frac{1}{2}{% endequation %}, גדולה ממעלת המכנה 0).

אפשר לטפל כך גם בסיטואציות מסובכות יותר. שורש {% equation %}n{% endequation %}-י של {% equation %}x{% endequation %} הוא המספר האי שלילי שמקיים {% equation %}a^{n}=x{% endequation %}, ומסמנים את זה {% equation %}a=\sqrt[n]{x}{% endequation %} או, בגישה שלנו, {% equation %}a=x^{\frac{1}{n}}{% endequation %}. ובאופן הכי כללי, {% equation %}x^{\frac{k}{n}}{% endequation %} הוא סימון מקוצר של {% equation %}\sqrt[n]{x^{k}}{% endequation %}. אלו לא פולינומים, אבל אלו עדיין חזקות של {% equation %}x{% endequation %} שאפשר להשוות את גודלן לחזקות אחרות של {% equation %}x{% endequation %}.

אם כן, נראה שכל תוספת השורשים הזו לא שינתה שום דבר מהותי ביחס למה שכבר ראינו.

אז זהו, שלא.

בואו נסתכל לרגע על הפונקציה {% equation %}f\left(x\right)=\frac{x}{\sqrt{x^{2}+4}}{% endequation %}. כאן העסק מתחיל להסתבך, כי השורש הוא לא על {% equation %}x{% endequation %} בודד אלא על ביטוי שלם. ומבט אחד בגרף של הפונקציה יבהיר לנו שאנחנו לא ברציוקנזס יותר:

<img src="{{site.baseurl}}{{site.post_images}}/2022/sqrt_complicated.png" alt=""/>

מה קורה כאן? ראשית, הפונקציה מוגדרת <strong>לכל</strong> {% equation %}x{% endequation %}, כי הביטוי שבתוך השורש, {% equation %}x^{2}+4{% endequation %}, הוא תמיד חיובי. יותר מכך, הוא שווה לפחות 4, ולכן השורש יהיה לפחות 2 ולכן המכנה לא יתאפס. שנית, לפונקציה יש <strong>שתי</strong> אסימפטוטות אופקיות שונות זו מזו: {% equation %}y=1{% endequation %} מימין ו-{% equation %}y=-1{% endequation %} משמאל.

מה האינטואיציה למה שקורה כאן? ובכן, {% equation %}\sqrt{x^{2}+4}{% endequation %} זה משהו שהוא "בערך כמו" {% equation %}x{% endequation %} מבחינת קצב הגידול שלו, כי השורש מקזז את ה-{% equation %}x^{2}{% endequation %} שיש בפנים. מכיוון שהמכנה הוא {% equation %}x{% endequation %} בעצמו, קיבלנו מקרה שדומה לזה של מונה ומכנה מאותה מעלה, ולכן האסימפטוטות נקבעות לפי מנת המקדמים המובילים. כאן העסק מתחיל להיות שונה. כאשר {% equation %}x\to\infty{% endequation %} המונה הוא חיובי וגם המכנה הוא חיובי ואין פלא שמתקרבים אל 1, אז כאשר {% equation %}x\to-\infty{% endequation %} קורה משהו שלא קרה קודם. המונה יהיה שלילי, אבל המכנה יהיה <strong>חיובי</strong>, בגלל שפונקציית השורש <strong>תמיד</strong> מחזירה את הערך החיובי. זה שונה לגמרי ממה שקרה בפונקציות רציונליות רגילות, שבהן אם גם המונה וגם המכנה היו שניהם מאותה מעלה, אז שניהם היו שליליים ביחד (אם המעלה הייתה אי זוגית) או ששניהם היו חיוביים ביחד (אם המעלה הייתה זוגית). כאן המונה שלילי והמכנה חיובי, ולכן התוצאה שאנחנו מקבלים היא אסימפטוטה {% equation %}y=-1{% endequation %}. ה-{% equation %}1{% endequation %} הוא עדיין מה שנובע מהיחס בין המקדם המוביל של המונה לזה של המכנה (אם למשל במונה היה {% equation %}3x{% endequation %} אז האסימפטוטות היו {% equation %}y=\pm3{% endequation %}), אבל הסימן השלילי שלו זה הדבר החדש שיכול לקרות כאן.

זה לכאורה מסיים עם {% equation %}f\left(x\right)=\frac{x}{\sqrt{x^{2}+4}}{% endequation %} אבל מרגיש לי מוזר לעצור פה. נפנפתי <strong>מאוד</strong> בידיים לגבי "{% equation %}\sqrt{x^{2}+4}{% endequation %} זה בערך אותו סדר גודל כמו {% equation %}x{% endequation %}" ואני מרגיש שזה זמן טוב להראות נימוק יותר משכנע, גם בלי לגלוש לפורמליזם המלא. אם כן, הבה ונראה מה עושים בחדו"א כדי להתמודד עם סיטואציות כאלו.

המהות של חדו"א היא פשוטה: <strong>לחסום, לחסום, לחסום</strong>. אם יש לנו ביטוי מסובך, אבל אנחנו יכולים להראות שהוא "כלוא" בין שני ביטויים פשוטים בהרבה, אנחנו מאוד שמחים. במקרה שלנו, ראשית נשים לב לכך ש-{% equation %}x^{2}\le x^{2}+4{% endequation %}, ולכן {% equation %}\sqrt{x^{2}}\le\sqrt{x^{2}+4}{% endequation %} (כאן אני משתמש בכך ששורש היא <strong>פונקציה עולה</strong>; ככל שמגדילים את הקלט שלה, גם הפלט גדל). אם אני מניח ש-{% equation %}x>0{% endequation %}, שזה מה שהולך לקרות בסיטואציה שבה {% equation %}x\to\infty{% endequation %}, אז {% equation %}\sqrt{x^{2}}=x{% endequation %}, כלומר קיבלתי {% equation %}x\le\sqrt{x^{2}+4}{% endequation %}. זה חסם בכיוון אחד.

מצד שני:

{% equation %}x^{2}+4\le x^{2}+4x+4=\left(x+2\right)^{2}{% endequation %}

כאן השתמשתי בכך שאני כבר מכיר את הנוסחה {% equation %}\left(x+a\right)^{2}=x^{2}+2ax+a^{2}{% endequation %}. מה המטרה שלי? למה הוספתי משהו ל-{% equation %}x^{2}+4{% endequation %} כדי לקבל ביטוי שכולו בריבוע? כמובן, כדי <strong>להיפטר מהשורש</strong> המעצבן הזה. קיבלתי:

{% equation %}\sqrt{x^{2}+4}\le\sqrt{\left(x+2\right)^{2}}=x+2{% endequation %}

אם כן, קיבלתי בסך הכל

{% equation %}x\le\sqrt{x^{2}+4}\le x+2{% endequation %}

זה כבר ממש מועיל. בואו ניזכר לרגע בחוק לגבי אי שוויונים שמערבים שברים: אם {% equation %}x\le y{% endequation %} אז {% equation %}\frac{1}{y}\le\frac{1}{x}{% endequation %}, כלומר כיוון האי-שוויון "מתהפך" אם מחלקים. לכן אי השוויון {% equation %}x\le\sqrt{x^{2}+4}\le x+2{% endequation %} שלנו הופך אל

{% equation %}\frac{1}{x}\ge\frac{1}{\sqrt{x^{2}+4}}\ge\frac{1}{x+2}{% endequation %}

וכדי שנקבל באמצע את {% equation %}f\left(x\right)=\frac{x}{\sqrt{x^{2}+4}}{% endequation %} אני כופל ב-{% equation %}x{% endequation %} את הכל. מכיוון שאני מניח ש-{% equation %}x\ge0{% endequation %} (כזכור, אנחנו כרגע במקרה של {% equation %}x\to\infty{% endequation %}) כיווני אי השוויון לא מתהפכים, וקיבלתי

{% equation %}\frac{x}{x+2}\le\frac{x}{\sqrt{x^{2}+4}}\le\frac{x}{x}{% endequation %}

עכשיו, {% equation %}\frac{x}{x}=1{% endequation %}, ומה בדבר {% equation %}\frac{x}{x+2}{% endequation %}? זו פונקציה רציונלית רגילה עם מונה ומכנה ששניהם ממעלה 1 ועם מקדם מוביל 1, ולכן {% equation %}\frac{x}{x+2}\underset{x\to\infty}{\to}1{% endequation %}. אז מה שקיבלנו הוא שהפונקציה {% equation %}\frac{x}{\sqrt{x^{2}+4}}{% endequation %} "כלואה" בין שתי פונקציות ששתיהן שואפות ל-1. לדבר כזה יש שם בחדו"א - <strong>משפט הסנדוויץ'</strong>. הוא אומר שאם יש לנו פונקציה ש"כלואה" בין שתי פונקציות ששואפות שתיהן לאותו גבול, גם הפונקציה שבאמצע שואפת לאותו הגבול. בכתיב קצת יותר פורמלי, אם {% equation %}g_{1}\left(x\right)\le f\left(x\right)\le g_{2}\left(x\right){% endequation %} וגם {% equation %}g_{1}\left(x\right)\to L{% endequation %} ו-{% equation %}g_{2}\left(x\right)\to L{% endequation %} אז גם {% equation %}f\left(x\right)\to L{% endequation %}.

אז במקרה הנוכחי קיבלנו ש-{% equation %}\frac{x}{\sqrt{x^{2}+4}}\underset{x\to\infty}{\to}1{% endequation %}. זו הדרך הפורמלית להוכיח שהאסימפטוטה הימנית היא {% equation %}y=1{% endequation %} (היא לא מלאה כי לא הוכחתי את משפט הסנדוויץ', אבל מן הסתם לא צריך להוכיח אותו בכל פעם שבה באים לחשב אסימפטוטה).

אני אסתכן עכשיו בטרחנות ואעשה את החישוב הדומה גם עבור {% equation %}x\to-\infty{% endequation %} פשוט כי עד עכשיו נפנפתי הרבה בידיים ואני רוצה שנראה בצורה מדויקת למה זה יוצא {% equation %}y=-1{% endequation %}.

אם כן, אני מניח עכשיו ש-{% equation %}x<0{% endequation %}. המקום הראשון שבו החישובים שעשיתי קודם "נשברים" הוא במעבר שלי מ-{% equation %}\sqrt{x^{2}}\le\sqrt{x^{2}+4}{% endequation %} אל {% equation %}x\le\sqrt{x^{2}+4}{% endequation %}. אם {% equation %}x<0{% endequation %} אז זה פשוט לא נכון ש-{% equation %}x=\sqrt{x^{2}}{% endequation %}, כי מה שפונקציית השורש מחזירה הוא תמיד השורש <strong>החיובי</strong>. מכיוון ש-{% equation %}x<0{% endequation %} הוא לא השורש החיובי של {% equation %}x^{2}{% endequation %}, אבל הוא <strong>כן </strong>מינוס השורש החיובי הזה. כלומר, אני יכול לכתוב {% equation %}x=-\sqrt{x^{2}}{% endequation %} ולהתקדם מכאן: מ-{% equation %}\sqrt{x^{2}}\le\sqrt{x^{2}+4}{% endequation %} אני מסיק {% equation %}-x\le\sqrt{x^{2}+4}{% endequation %}.

עבור הכיוון השני, המעבר {% equation %}x^{2}+4\le x^{2}+4x+4{% endequation %} כבר לא נכון כי כאשר {% equation %}x<0{% endequation %} אז {% equation %}4x<0{% endequation %}, אבל מצד שני {% equation %}-4x>0{% endequation %} אז אני יכול לכתוב

{% equation %}x^{2}+4\le x^{2}-4x+4=\left(-x+2\right)^{2}{% endequation %}

ומכיוון שהביטוי {% equation %}\left(-x+2\right){% endequation %} חיובי אני יכול לכתוב {% equation %}\sqrt{\left(-x+2\right)^{2}}=-x+2{% endequation %}. קיבלתי

{% equation %}-x\le\sqrt{x^{2}+4}\le-x+2{% endequation %}

ואחרי שניקח את ההופכי של כולם, נקבל

{% equation %}-\frac{1}{x}\ge\frac{1}{\sqrt{x^{2}+4}}\ge-\frac{1}{x+2}{% endequation %}

ועכשיו אני כופל את זה ב-{% equation %}x{% endequation %}. הפעם {% equation %}x<0{% endequation %} ולכן כיוון אי השווינים <strong>כן</strong> מתהפך:

{% equation %}-\frac{x}{x}\le\frac{x}{\sqrt{x^{2}+4}}\le-\frac{x}{x+2}{% endequation %}

ועכשיו יש לי שוב את כלל הסנדוויץ', אבל הפעם כששתי הפונקציות בצדדים שואפות אל {% equation %}-1{% endequation %}, מה שמסיים את ההוכחה.

יופי, התקדמנו! אנחנו גם קצת יותר מתורגלים בעבודה עם שורשים, וגם ראינו כלי רציני שאפשר להשתמש בו כדי לחשב אסימפטוטות אופקיות. כאן עולה כמובן השאלה - האם זה כלי שאפשר להשתמש בו <strong>בבית הספר</strong>? אני מודה שאני לא יודע. אני חושד שלא, ושהתיאור ה"אינטואיטיבי" הוא מה שאמורים להסתמך עליו, בנוסף אולי להצבה של ערכים גדולים וקטנים של {% equation %}x{% endequation %} ובחינה של מה קורה.

<h2>אסימפטוטות שמערבות לוגריתמים</h2>

עכשיו בואו נסבך את התמונה על ידי סוג חדש של פונקציה שטרם הזכרתי - <strong>לוגריתמים</strong>. <a href="https://gadial.net/2020/06/08/what_are_logarithms/">יש לי פוסט על לוגריתמים</a> אז אני אזכיר רק בקצרה מה הם: אם {% equation %}x=10^{a}{% endequation %} אז {% equation %}\log x=a{% endequation %}. כלומר, {% equation %}\log{% endequation %} של מספר כלשהו אומר "באיזו חזקה צריך להעלות את 10 כדי לקבל את {% equation %}x{% endequation %}?". כאן החזקה יכולה להיות כל מספר - חיובי, שלילי, שלם, שבר, אפילו {% equation %}\pi{% endequation %}.

ההגדרה של {% equation %}\log{% endequation %} שהצגתי מתבססת על 10, אבל 10 הוא מספר די שרירותי - אנחנו משתמשים בו כנראה כי יש לנו 10 אצבעות, אבל אין מניעה לדבר על לוגריתמים שמדברים על העלאה בחזקה של מספרים אחרים. למספר שבודקים כמה צריך להעלות אותו בחזקה קוראים <strong>בסיס הלוגריתם</strong>. אנחנו ראינו לוגריתם שהבסיס שלו הוא 10, אבל עוד סוג מאוד נפוץ הוא לוגריתם על בסיס 2, שקיבל סימון משלו: {% equation %}\lg{% endequation %}. כך למשל {% equation %}\lg256=8{% endequation %} כי {% equation %}2^{8}=256{% endequation %}. ואפשר להשתמש בעוד בסיסים גם אם אין להם סימון מיוחד: למשל, {% equation %}\log_{6}36{% endequation %} הוא הסימון ללוגריתם על בסיס 6 של 36, וזה שווה 2, כי {% equation %}6^{2}=36{% endequation %}. מה שכן קריטי הוא שהבסיס יהיה תמיד <strong>מספר גדול מ-</strong><strong>1</strong> כי כשמעלים בחזקה מספרים קטנים או שווים מ-1 מתחילות להתרחש כל מני מהומות שאין לנו כוח אליהן.

אבל עזבו אתכם מבסיס 2, או 6, או 10. יש בסיס אחד שבשימוש נרחב משמעותית יותר מכל בסיס אחר: בסיס שהוא המספר {% equation %}e=2.718281828459\ldots{% endequation %}, מה שכמובן מעורר שאלת "מה הולך פה?!" אצל מי שרואים את זה בפעם הראשונה.

במקום לכתוב {% equation %}\log_{e}{% endequation %} אנחנו כותבים {% equation %}\ln{% endequation %}, וזה יהיה הסימון שבו אני אשתמש בהמשך כל הזמן. לפני שאסביר <strong>למה</strong> אנחנו משתמשים ב-{% equation %}\ln{% endequation %} הזה ולא סתם ב-{% equation %}\log{% endequation %} אני אתחיל עם להבהיר ש<strong>זה לא משנה</strong> באיזה לוגריתם אנחנו משתמשים כי כולם פחות או יותר אותו הדבר. אחת התוצאות הבסיסיות על לוגריתמים היא השוויון {% equation %}\log_{a}b=\frac{\ln b}{\ln a}{% endequation %}, שאומר שבעצם, לכל {% equation %}a{% endequation %} אפשרי, הלוגריתם על בסיס {% equation %}a{% endequation %} הוא "כמו {% equation %}\ln{% endequation %} רק כפול איזה קבוע". למשל, עבור {% equation %}a=10{% endequation %}, אנחנו מקבלים ש-{% equation %}\log b=\left(\frac{1}{\ln10}\right)\ln b{% endequation %}, כלומר כדי לחשב את {% equation %}\log b{% endequation %} אנחנו מחשבים את {% equation %}\ln b{% endequation %} ופשוט כופלים במספר הקבוע {% equation %}\frac{1}{\ln10}{% endequation %}.

אז למה בעצם להשתמש במספר מוזר כמו {% equation %}e{% endequation %} זה הדבר הנכון? יש הרבה גישות שונות שבהן הוא צץ, אבל אני אלך על הישירה ביותר - זו שמערבת את מושג <strong>הנגזרת</strong> שלומדים בחדו"א ומתאר את קצב השינוי של פונקציות. אם אנחנו גוזרים את {% equation %}\ln x{% endequation %} אנחנו מקבלים את הנגזרת הנחמדה {% equation %}\frac{1}{x}{% endequation %}. אם לעומת זאת אנחנו גוזרים לוגריתם בבסיס אחר {% equation %}a{% endequation %}, כלומר את {% equation %}\log_{a}x{% endequation %}, אנחנו מקבלים {% equation %}\frac{1}{x\ln a}{% endequation %} - משתרבב לנו פנימה עוד איזה קבוע. באופן דומה אפשר לדבר על מה שנקרא <strong>פונקציה אקספוננציאלית</strong> שהיא פונקציה מהצורה {% equation %}f\left(x\right)=a^{x}{% endequation %} - כזו שבו לוקחים את {% equation %}x{% endequation %} ובמקום להעלות <strong>אותו</strong> בחזקה כמו שעושים בפולינומים, להשתמש בו דווקא בתור המעריך של חזקה שהבסיס שלה הוא מספר {% equation %}a{% endequation %} נתון מראש. אז גם בפונקציה כזו, הנגזרת שלה תהיה {% equation %}a^{x}\ln\left(a\right){% endequation %} - מוכפלת בקבוע. אם אנחנו בוחרים {% equation %}a=e{% endequation %} אז נקבל שהנגזרת של {% equation %}e^{x}{% endequation %} היא {% equation %}e^{x}{% endequation %} עצמה - הפונקציה היחידה ששווה לנגזרת שלה. למעשה, זו דרך פופולרית להגדיר את {% equation %}e{% endequation %}: מוכיחים (עם כלים מתקדמים יחסית בחדו"א) שקיימת רק פונקציה אחת {% equation %}f\left(x\right){% endequation %} ששווה לנגזרת של עצמה ומקיימת {% equation %}f\left(0\right)=1{% endequation %}, ואז מגדירים {% equation %}e=f\left(1\right){% endequation %} ומוכיחים שהפונקציה הזו מתנהגת כמו {% equation %}e^{x}{% endequation %}.

נחזור לעניין שלשמו התכנסנו - אסימפטוטות. כרגיל, הכי טוב להסתכל קודם כל על הגרף של {% equation %}\ln x{% endequation %} כדי לקבל תחושה מה קורה פה:

<img src="{{site.baseurl}}{{site.post_images}}/2022/lnx.png" alt=""/>

מה שאפשר לראות פה מייד הוא שכאשר הפונקציה מתקרבת אל {% equation %}x=0{% endequation %} היא צוללת בחדות למטה - יש לה <strong>אסימפטוטה אנכית</strong>. הסיבה לכך היא שככל שמספר קרוב יותר לאפס, כך גם החזקה שבה צריך להעלות את {% equation %}e{% endequation %} כדי לקבל אותו היא נמוכה יותר (את אפס עצמו אי אפשר להשיג אף פעם, ולכן הפונקציה לא מוגדרת ב-{% equation %}x=0{% endequation %}). לעומת זאת, כשמסתכלים מה קוה עם {% equation %}x\to\infty{% endequation %} הסיטואציה דומה למה שקרה עם שורש - לא ברור אם יש אסימפטוטה אופקית או לא. קצת מחשבה מראה שלא יכולה להיות כזו: אם נסתכל על {% equation %}y=a{% endequation %}, אז קיימת חזקה כלשהי של {% equation %}e{% endequation %} שמקיימת {% equation %}e^{x}>a{% endequation %} (כי ככל שמגדילים את {% equation %}x{% endequation %} כך {% equation %}e^{x}{% endequation %} גדל באופן בלתי חסום) ולכן עבור {% equation %}x=\ln a{% endequation %} ומעלה, הפונקציה תחצה את {% equation %}y=a{% endequation %} ותמשיך להתרחק ממנו.

במקרה של שורש ראינו שאפשר לחשוב עליו בתור {% equation %}x^{\frac{1}{2}}{% endequation %} ולהשוות אותו עם פולינומים. עבור לוגריתם הסיטואציה קצת שונה - <strong>כל</strong> ביטוי מהצורה {% equation %}x^{a}{% endequation %} עבור {% equation %}a>0{% endequation %} גדל "יותר מהר" מ-{% equation %}\ln x{% endequation %}. כלומר, אם יש לנו {% equation %}\frac{\ln x}{x}{% endequation %}, אז כש-{% equation %}x\to\infty{% endequation %} הביטוי הזה ישאף לאפס. לעומת זאת, השאיפה ל-{% equation %}-\infty{% endequation %} של {% equation %}\ln x{% endequation %} כש-{% equation %}x\to0^{+}{% endequation %} חזקה יותר מכל פולינום, כך ש-{% equation %}\frac{\ln x}{x}\underset{x\to0^{+}}{\to}-\infty{% endequation %}.

מאיפה אני יודע את הדברים הללו? לצערי, אין לי כאן כלל סנדוויץ' לשלוף; ההוכחות שאני מכיר מתבססות על כלי חזק בחדו"א שנקרא <strong>כלל לופיטל</strong> ומשתמש בנגזרות, שזה מושג שאני לא ממש נכנס אליו כאן. ניאלץ פשוט לקבל את הטענות הללו כנכונות.

בואו נראה עכשיו משהו קצת יותר מסובך כדי להבין את העיקרון הכללי של איך לטפל בדברים מסובכים (אבל כמובן, מה שיש בפוסטים הללו לא מספיק; צריך לתרגל עוד ולראות עוד דוגמאות): הפונקציה {% equation %}\ln\left(x^{2}-4\right){% endequation %}. פונקציה כזו נקראת "הרכבה" - אנחנו לוקחים את הפולינום {% equation %}x^{2}-4{% endequation %} ו"מרכיבים" אותו על הפונקציה {% equation %}\ln{% endequation %}. כלומר, במקום ה-{% equation %}x{% endequation %} הרגיל שהוא קלט של {% equation %}\ln{% endequation %}, מה ש-{% equation %}\ln{% endequation %} מקבלת הוא את כל הפולינום.

כזכור, {% equation %}\ln x{% endequation %} בכלל לא מוגדר אם {% equation %}x\le0{% endequation %}. אז {% equation %}\ln\left(x^{2}-4\right){% endequation %} בכלל לא מוגדר אם {% equation %}x^{2}-4\le0{% endequation %}, כלומר אם {% equation %}x^{2}\le4{% endequation %}, כלומר אם {% equation %}-2\le x\le2{% endequation %}. האסימפטוטה של {% equation %}\ln x{% endequation %} צצה כש-{% equation %}x{% endequation %} שואף אל 0, אז עבור {% equation %}\ln\left(x^{2}-4\right){% endequation %} היא תצוץ כש-{% equation %}x^{2}-4{% endequation %} ישאף אל אפס. בפונקציה נחמדה כמו פולינום קל לדעת מתי היא שואפת לאנשהו - בודקים באיזו נקודה היא <strong>שווה בדיוק</strong> לאותו משהו, ואז כששואפים לנקודה הזו, הפונקציה שואפת למשהו (ה"נחמדות" הזו נקראת <strong>רציפות</strong>; כל הפולינומים רציפים, פונקציות רציונליות רציפות בכל נקודה שבה הן מוגדרות, שורשים, לוגריתמים וגם פונקציות טריגונומטריות - כולן רציפות!).

{% equation %}x^{2}-4=0{% endequation %} בדיוק כאשר {% equation %}x=\pm2{% endequation %}, ולכן כש-{% equation %}x\to2^{+}{% endequation %} ו-{% equation %}x\to-2^{-}{% endequation %} הפונקציה תשאף אל {% equation %}-\infty{% endequation %} וקיבלנו שתי אסימפטוטות אנכיות, ב-{% equation %}x=\pm2{% endequation %}. למה כתבתי {% equation %}x\to2^{+}{% endequation %}? הפלוס הזה אומר שאני שואף אל 2 מצד ימין - מהצד החיובי שלה - כי מהצד השמאלי הפונקציה לא מוגדרת. בדומה גם עבור {% equation %}-2{% endequation %} שאליה אני שואף מצד שמאל.

אגב, מה קורה עם הפונקציה {% equation %}f\left(x\right)=e^{x}{% endequation %}? האם לה יש אסימפטוטות? אם נציץ בגרף שלה נגלה שהיא נראית כאילו לקחנו את הגרף של {% equation %}\ln x{% endequation %}, סובבנו אותו 90 מעלות נגד כיוון השעון, ואז בנוסף לכל הצרות גם שיקפנו בראי:

<img src="{{site.baseurl}}{{site.post_images}}/2022/ex.png" alt=""/>

הדמיון הזה לא מקרי; הוא נובע מכך ש-{% equation %}e^{x}{% endequation %} ו-{% equation %}\ln x{% endequation %} הן פונקציות הופכיות זו לזו, כלומר אם מפעילים אחת ואז את השניה חוזרים לערך המקורי. הקטע הזה של "הגרף מתקבל מסיבוב ושיקוף" נכון באופן כללי לכל זוג פונקציות הופכיות.

עכשיו, כאשר {% equation %}x\to\infty{% endequation %} הגרף של {% equation %}e^{x}{% endequation %} מתנהג כמו החלק הלא אסימפטוטי של הגרף של {% equation %}\ln x{% endequation %} - כל מה שקורה הוא ש-{% equation %}e^{x}\to\infty{% endequation %} ואין פה אסימפטוטה. אבל כאשר {% equation %}x\to-\infty{% endequation %} יש לנו את האסימפטוטה האופקית {% equation %}y=0{% endequation %}, בדיוק כמו שב-{% equation %}\ln x{% endequation %} הייתה לנו האסימפטוטה האנכית {% equation %}x=0{% endequation %} (הסיבוב ב-90 מעלות המדובר הופך אסימפטוטה אנכית לאופקית).

<h2>אסימפטוטות שמערבות פונקציות טריגונומטריות</h2>

יש לי <a href="https://gadial.net/2021/05/13/trigonometry_intro/">פוסטים</a> על טריגונומטריה, אז בואו ניגש מייד לעסק: שתי הפונקציות המרכזיות שלנו הן <strong>סינוס</strong> ו<strong>קוסינוס</strong>, {% equation %}\sin x,\cos x{% endequation %}, שהן פונקציות <strong>מחזוריות</strong> שנעות בין {% equation %}1{% endequation %} ובין {% equation %}-1{% endequation %}, ובעצם נראות אותו דבר בדיוק חוץ מזה שאחת היא הזזה של השניה:

<img src="{{site.baseurl}}{{site.post_images}}/2022/trigo_func.png" alt=""/>

הפונקציה שעוברת בראשית הצירים היא סינוס, וזו שב-{% equation %}x=0{% endequation %} שווה 1 דווקא היא קוסינוס. אלו פונקציות מרכזיות במתמטיקה ובחיים ובהכל, אבל נראה שהרלוונטיות שלהן לדיון האסימפטוטות היא כמעט אפסית - הן בוודאי לא שואפות לשום נקודה קונקרטית כש-{% equation %}x{% endequation %} שואף לאינסוף, והן לא "מתפוצצות" עם אסימפטוטה אנכית. בפוסט הקודם ראינו שהסיטואציה שלהן כשמערבים אותן בפונקציות רציונליות היא בעייתית יותר: {% equation %}\frac{\sin x}{x}{% endequation %} הידועה לשמצה היא פונקציה שבסביבות {% equation %}0{% endequation %} שואפת ל-1 ואין לה אסימפטוטה, ואילו כאשר {% equation %}x{% endequation %} שואף לאינסוף היא שואפת לאפס. אינטואיטיבית, הסיבה לכך היא שקרוב מאוד לאפס, {% equation %}\sin x{% endequation %} מתנהגת מאוד דומה ל-{% equation %}x{% endequation %}, אבל הדמיון הזה הולך לאיבוד לחלוטין אחרי שמתרחקים קצת מאפס.

ושוב, אפשר לשאול - איך מוכיחים את זה? בפרט, איך מוכיחים ש-{% equation %}\frac{\sin x}{x}\underset{x\to0}{\to}1{% endequation %}? באופן אולי מפתיע, זו הוכחה <strong>מאוד לא פשוטה</strong> (<a href="https://gadial.net/2008/01/20/lim_sin_x_over_x/">יש לי פוסט</a> שמסביר מה בעצם הבעיה פה) והגבול הלכאורה תמים הזה הוא בעצם בעל חשיבות <strong>קריטית</strong> לחדו"א של פונקציות טריגונומטריות; עליו מתבססים כשמחשבים את הנגזרות שלהן.

אם כן, אין משהו מעניין לומר על אסימפטוטות וטריגונומטריה... רגע, חכו חכו. יש עוד פונקציה טריגונומטרית אחת שלא הזכרתי - <strong>טנגנס</strong>. היא מוגדרת פשוט בתור {% equation %}\tan x=\frac{\sin x}{\cos x}{% endequation %}. עכשיו, הקוסינוס שבמכנה מתאפס די הרבה וכשזה קורה הסינוס לא נמצא בסביבות אפס בכלל, כלומר אנחנו הולכים לקבל אסימפטוטה. ולא אחת, אלא הרבה - בגלל המחזוריות של סינוס וקוסינוס, גם האסימפטוטות של טנגנס יהיו מחזוריות. ככה זה נראה:

<img src="{{site.baseurl}}{{site.post_images}}/2022/tan.png" alt=""/>

טנגנס היא פונקציה שחוזרת על עצמה הרבה פעמים, ובכל פעם כזו הצד השמאלי שלה שואף ל-{% equation %}-\infty{% endequation %} והימני שואף ל-{% equation %}\infty{% endequation %}. באילו נקודות זה קורה? ובכן, יש פיצוץ בכל פעם שבה המכנה של {% equation %}\frac{\sin x}{\cos x}{% endequation %} שואף לאפס. ומתי זה קורה? כאמור, {% equation %}\cos x{% endequation %} רציפה, אז זה קורה בדיוק כש-{% equation %}x{% endequation %} שואף לערך שבו {% equation %}\cos x=0{% endequation %}. ומתי <strong>זה</strong> קורה? ובכן, זה מצריך אותי להכניס לתמונה את הקבוע המפורסם השני של המתמטיקה: {% equation %}\pi=3.14159265359{% endequation %}. איך הוא קשור? 

ובכן, הנה דרך אפשרית אחת לחשוב על קוסינוס: נצייר מעגל עם רדיוס 1, נעמוד עליו בנקודה {% equation %}\left(1,0\right){% endequation %} (הימנית ביותר) ואז נתחיל ללכת עליו נגד כיוון השעון ונסמן את המרחק שהלכנו עד כה ב-{% equation %}x{% endequation %}. בכל רגע נתון אפשר לעצור ולבדוק לאן הגענו. נניח שהגענו לקואורדינטה {% equation %}\left(a,b\right){% endequation %} כלשהי; אז {% equation %}a=\cos x{% endequation %}.

<img src="{{site.baseurl}}{{site.post_images}}/2022/circle_cos.png" alt=""/>

זו לא הדרך הכי מיידית לתאר קוסינוס, אבל היא בהחלט נכונה ועובדת, ומאפשרת לנו לראות מה הקשר של {% equation %}\pi{% endequation %} לכל זה. בבסיסו, {% equation %}\pi{% endequation %} הוא היחס בין היקף מעגל והקוטר שלו: אם למעגל יש רדיוס 1 אז הקוטר שלו הוא 2, ולכן ההיקף שלו הוא {% equation %}2\pi{% endequation %}. זה היקף של מעגל שלם, ולכן היקף של <strong>רבע</strong> מעגל הוא {% equation %}\frac{\pi}{2}{% endequation %}. הפעם הראשונה בטיול שלנו על המעגל שבה אנחנו מגיעים לקואורדינטה {% equation %}\left(a,b\right){% endequation %} עם {% equation %}a=0{% endequation %} (כלומר, חוצים את ציר {% equation %}y{% endequation %}) היא כאשר השלמנו טיול על רבע מעגל בדיוק: {% equation %}\cos\left(\frac{\pi}{2}\right)=0{% endequation %}. הפעם השניה היא כשהשלמנו סיבוב על חצי המעגל שמצד שמאל של ציר {% equation %}y{% endequation %}; חצי מעגל הוא מאורך {% equation %}\pi{% endequation %} כך שקיבלנו {% equation %}\cos\left(\frac{\pi}{2}+\pi\right)=0{% endequation %}, וזה הולך להימשך - בכל פעם, אחרי שאנחנו מבצעים עוד מסע באורך {% equation %}\pi{% endequation %} נגיע אל ציר {% equation %}y{% endequation %}. ולכן באופן כללי אפשר לכתוב {% equation %}\cos\left(\frac{\pi}{2}+\pi k\right)=0{% endequation %} וזה לכל {% equation %}k\in\mathbb{Z}{% endequation %} (גם עבור מספרים שליליים זה עובד!) לכן האסימפטוטות של {% equation %}\tan x{% endequation %} יהיו בנקודות {% equation %}x=\frac{\pi}{2}+\pi k{% endequation %} הללו.

זה מספיק כדי להבין את הרעיון הבסיסי של התעסקות עם פונקציות טריגונומטריות, אבל כמובן שתמיד יש סיבוכים. למשל, אם {% equation %}f\left(x\right)=\frac{\cos x}{\cos x+1}{% endequation %}, מה קורה כאן? במונה ובמכנה יש {% equation %}\cos x{% endequation %} וזה אולי קצת מזכיר את המקרה של {% equation %}\frac{x}{x+1}{% endequation %} שיש לו אסימפטוטות אופקיות, אבל במקרה של הפונקציות הטריגונומטריות זה לא קורה כי כזכור, {% equation %}\cos x{% endequation %} מזפזפת לה בין {% equation %}1{% endequation %} ובין {% equation %}-1{% endequation %} ולכן ההתנהגות שלה כש-{% equation %}x{% endequation %} שואף לאינסוף לא שונה מההתנהגות שלה בסביבות {% equation %}x=0{% endequation %}.

מה עם אסימפטוטות אנכיות? כאן צריך לראות מתי {% equation %}\cos x+1=0{% endequation %}, כלומר {% equation %}\cos x=-1{% endequation %}, וזו כבר משוואה שונה מזו שדיברתי עליה קודם, אבל הרעיון הוא דומה: {% equation %}\cos x=-1{% endequation %} אם אחרי ה"טיול" על המעגל הגענו אל הנקודה {% equation %}\left(-1,0\right){% endequation %} (זו הנקודה <strong>היחידה</strong> על המעגל שקואורדינטת ה-{% equation %}x{% endequation %} שלה היא {% equation %}-1{% endequation %}). מכיוון שהתחלנו בדיוק בצד השני של המעגל, הגענו לנקודה הזו אחרי מרחק {% equation %}\pi{% endequation %}, כלומר {% equation %}\cos\left(\pi\right)=-1{% endequation %}. כמו כן, אנחנו חוזרים לנקודה הזו כל {% equation %}2\pi{% endequation %} צעדים (ולא כל {% equation %}\pi{% endequation %} צעדים כי כאמור - יש רק נקודה אחת כזו, להבדיל מהמקרה הקודם שבו היו <strong>שתי</strong> נקודות עם קואורדינטת ה-{% equation %}x{% endequation %} המתאימה שהמרחק ביניהן על המעגל היה בדיוק {% equation %}\pi{% endequation %}). לכן יש אסימפטוטה אופקית בכל הנקודות {% equation %}x=\pi+2k\pi{% endequation %}.

<h2>ומה ההסבר הפורמלי לכל זה?</h2>

אני רוצה לעשות "תם ולא נשלם", כי הפוסט הזה הציג את הרעיונות הכלליים של אסימפטוטות אבל בוודאי שלא נכנס לכל החישובים והסיטואציות האפשריות, כולל אלו שרואים בבית הספר; ועדיין, אני מקווה שהוא עוזר מספיק כדי לקבל את המושג הראשוני של מה הולך כאן בכלל ומי הנפשות הפועלות.

אבל אני לא רוצה לסיים בלי להציג את הפורמליזם האמיתי שעומד מאחורי כל זה, פשוט כי אני זוכר כמה הפריע לי, כתלמיד תיכון שקרא ספרי מתמטיקה, שפטרו דברים כמו הגדרת הגבול ב"לא נוכל כאן להציג את הגדרת הגבול" ואז המשיכו להשתמש בגבולות כמו כלום, כמו שעשינו כאן. אז אני אכתוב פה הסברים קצרים ותמציתיים יחסית; יש לי <a href="https://gadial.net/2010/10/26/limit_of_functions_and_continuity/">פוסטים מלאים יותר</a> בנושאים הללו.

המושג הבסיסי שעליו כל נושא האסימפטוטות מתבסס הוא מושג ה<strong>גבול</strong>. גבול של פונקציה מתאר "לאן הפלט של הפונקציה הולך כשהקלט הולך למקום ספציפי". ההגדרה המדויקת של גבול היא לא קלה לעיכול ולכן נמנעים ממנה בבתי הספר, אבל קל לכתוב את כולה בשורה אחת:

אומרים ש-{% equation %}f\left(x\right){% endequation %} שואפת לגבול {% equation %}L{% endequation %} כאשר {% equation %}x{% endequation %} שואף ל-{% equation %}x_{0}{% endequation %} ומסמנים את זה בתור {% equation %}f\left(x\right)\underset{x\to_{x0}}{\to}L{% endequation %}, או בסימון החביב עלי יותר שהסתרתי עד כה, {% equation %}\lim_{x\to x_{0}}f\left(x\right)=L{% endequation %}, אם:

לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}\delta>0{% endequation %} כך שאם {% equation %}\left|x-x_{0}\right|<\delta{% endequation %} אז {% equation %}\left|f\left(x\right)-L\right|<\varepsilon{% endequation %}

או במילים: לכל אפסילון גדול מאפס אנחנו יכולים למצוא דלתא גדול מאפס, כך שאם <strong>המרחק</strong> של {% equation %}x{% endequation %} מ-{% equation %}x_{0}{% endequation %} קטן מדלתא, אז המרחק של {% equation %}f\left(x\right){% endequation %} מ-{% equation %}L{% endequation %} קטן מאפסילון.

כשאנחנו מתעסקים עם אסימפטוטות, אנחנו עובדים עם הכללה של ההגדרה הזו שגם מערבת את מושג ה<strong>אינסוף</strong>. בחדו"א נזהרים לא להגדיר דברים תוך התייחסות לאינסוף בתור מספר, אלא בתור סימון בלבד, וזה יוביל אותנו לכמה הגדרות שהן כולן באותה הרוח:

<ul> <li>{% equation %}\lim_{x\to\infty}f\left(x\right)=L{% endequation %} אם לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}M>0{% endequation %} כך שאם {% equation %}x>M{% endequation %} אז {% equation %}\left|f\left(x\right)-L\right|<\varepsilon{% endequation %}</li>


<li>{% equation %}\lim_{x\to-\infty}f\left(x\right)=L{% endequation %} אם לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}M>0{% endequation %} כך שאם {% equation %}x<-M{% endequation %} אז {% equation %}\left|f\left(x\right)-L\right|<\varepsilon{% endequation %}</li>


<li>{% equation %}\lim_{x\to x_{0}}f\left(x\right)=\infty{% endequation %} אם לכל {% equation %}M>0{% endequation %} קיים {% equation %}\delta>0{% endequation %} כך שאם {% equation %}\left|x-x_{0}\right|<\delta{% endequation %} אז {% equation %}f\left(x\right)>M{% endequation %}</li>


<li>{% equation %}\lim_{x\to x_{0}}f\left(x\right)=-\infty{% endequation %} אם לכל {% equation %}M>0{% endequation %} קיים {% equation %}\delta>0{% endequation %} כך שאם {% equation %}\left|x-x_{0}\right|<\delta{% endequation %} אז {% equation %}f\left(x\right)<-M{% endequation %}</li>

</ul>

את זה אפשר לסבך עוד יותר - שגם השאיפה של {% equation %}x{% endequation %} תהיה לאינסוף/מינוס אינסוף וגם הפונקציה עצמה שואפת לאינסוף תוך כדי, ואפשר גם לדבר על שאיפה "חד צדדית" ל-{% equation %}x_{0}{% endequation %}, למשל {% equation %}x\to x_{0}^{+}{% endequation %} אומר שבמקום הדרישה {% equation %}\left|x-x_{0}\right|<\delta{% endequation %} שבעצם אומרת {% equation %}x_{0}-\delta<x<x_{0}+\delta{% endequation %}, תהיה לנו רק הדרישה {% equation %}x_{0}<x<x_{0}+\delta{% endequation %}, וכדומה.

אם יש לנו שתי פונקציות {% equation %}f\left(x\right),g\left(x\right){% endequation %}, אפשר לדבר גם על המרחק ביניהן לכל {% equation %}x{% endequation %}: זה פשוט {% equation %}\left|f\left(x\right)-g\left(x\right)\right|{% endequation %}. הדבר הזה הוא בעצמו פונקציה של {% equation %}x{% endequation %}; אני יכול למשל לסמן {% equation %}h\left(x\right)=\left|f\left(x\right)-g\left(x\right)\right|{% endequation %}. עכשיו, אם {% equation %}\lim_{x\to\infty}h\left(x\right)=0{% endequation %}, המשמעות היא שהפונקציות {% equation %}f,g{% endequation %} "שואפות אחת לשניה" כש-{% equation %}x{% endequation %} שואף לאינסוף. אני אחשוב על {% equation %}f{% endequation %} בתור הפונקציה הרגילה שלנו ועל {% equation %}g{% endequation %} בתור קו ישר, ועולה השאלה - איך בעצם נראית פונקציה של קו ישר? התשובה פשוטה: {% equation %}g\left(x\right)=mx+a{% endequation %}, כאשר הקבוע {% equation %}m{% endequation %} נקרא <strong>השיפוע</strong> של הישר ואילו {% equation %}a{% endequation %} היא נקודת החיתוך עם ציר {% equation %}y{% endequation %} (כי {% equation %}g\left(0\right)=a{% endequation %}, ו-{% equation %}x=0{% endequation %} בדיוק כשאנחנו עוברים דרך ציר {% equation %}y{% endequation %}).

עד עכשיו ראינו שני סוגים של קווים: ראשית, קווים אופקיים, שבהם {% equation %}m=0{% endequation %}; ושנית, קווים אנכיים שבהם... אה... {% equation %}m=\infty{% endequation %}? לא אמרתי לפני רגע שאסור לי לעשות משהו כזה? ובכן, כן; קווים אנכיים הם סוג של יוצאים מן הכלל כי הם הקווים היחידים שאינם <strong>פונקציות</strong>. בפונקציה, לכל קואורדינטת {% equation %}x{% endequation %} יש ערך בודד של {% equation %}y{% endequation %} שמתאים לה; אבל בקו אנכי לכל הנקודות אותה קואורדינטת {% equation %}x{% endequation %}. העניין הוא שלא <strong>חייבים</strong> להשתמש בפונקציות כדי לתאר אובייקטים גאומטריים; הדרך הכללית לתאר אותם היא באמצעות <strong>משוואה</strong>.

על הפונקציה {% equation %}y=mx+a{% endequation %} אפשר לחשוב גם בתור משוואה, {% equation %}y-mx-a=0{% endequation %}. זה מוביל אותנו להגדרה ה"כללית" של ישר: אוסף הפתרונות {% equation %}\left(x,y\right){% endequation %} של משוואה מהצורה {% equation %}Ax+By+C=0{% endequation %} כאשר {% equation %}A,B,C{% endequation %} הם פרמטרים. בפרט, אוסף הפתרונות של המשוואה {% equation %}x=a{% endequation %} הוא ישר - הישר האנכי שחותך את ציר {% equation %}x{% endequation %} בנקודה {% equation %}a{% endequation %}.

אם אנחנו רוצים לבדוק האם יש לפונקציה אסימפטוטה אופקית כש-{% equation %}x{% endequation %} שואף לאינסוף, אנחנו בעצם בודקים האם קיים {% equation %}a{% endequation %} כך ש-{% equation %}\left|f\left(x\right)-g\left(x\right)\right|\underset{x\to\infty}{\to}0{% endequation %} עבור {% equation %}g\left(x\right)=a{% endequation %}, כלומר האם {% equation %}\left|f\left(x\right)-a\right|\underset{x\to\infty}{\to}0{% endequation %}. אם נפתח את הגדרת הגבול בצורה מלאה נראה שאנחנו שואלים האם לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}M{% endequation %} כך שאם {% equation %}x>M{% endequation %} אז {% equation %}\left|f\left(x\right)-a-0\right|<\varepsilon{% endequation %} שזה בעצם אותו הדבר בדיוק כמו לומר ש-{% equation %}f\left(x\right)\underset{x\to\infty}{\to}a{% endequation %}. במילים אחרות, הבעיה של מציאת אסימפטוטה <strong>אופקית</strong> לפונקציה היא בדיוק אותה בעיה כמו לבדוק האם לפונקציה קיים גבול באינסוף. אולי זו הסיבה למה מאז שהתחלתי ללמוד חדו"א באוניברסיטה לא זכור לי שדיברו על אסימפטוטות יותר - פשוט מדברים על גבולות וזהו.

בשביל אסימפטוטה אנכית אנחנו צריכים לבדוק האם קיים {% equation %}a{% endequation %} שעבורו {% equation %}\lim_{x\to a^{\pm}}f\left(x\right)=\pm\infty{% endequation %} (הפלוס/מינוס כאן אומר "או זה או זה"; יש 4 שילובים אפשריים של כיוון השאיפה אל {% equation %}a{% endequation %} והאם הפונקציה שואפת לאינסוף או מינוס אינסוף).

לפונקציה יש לכל היותר שתי אסימפטוטות אופקיות - אחת לכיוון {% equation %}\infty{% endequation %} והשניה לכיוון {% equation %}-\infty{% endequation %}. זאת מכיוון שהגבול של פונקציה בשאיפה לנקודה מסויימת או לאינסוף הוא <strong>יחיד</strong>, בהנחה שהוא קיים. לעומת זאת כפי שראינו עם טנגנס, יכולות להיות אינסוף אסימפטוטות אנכיות - כי פונקציה יכולה לשאוף לאינסוף בכמה נקודות שונות (בכל נקודה כזו הגבול הוא עדיין יחיד - אינסוף).

אז האם סיימנו? לא!

<h2>בונוס: עוד אסימפטוטות!</h2>

ההגדרה הפורמלית שנתתי מאפשרת לי לדבר על משהו שעד עכשיו הסתרתי לגמרי - יש גם אסימפטוטות שאינן אופקיות או אנכיות אלא <strong>משופעות</strong>; כל קו ישר יכול לתפקד בתור אסימפטוטה. בואו נראה דוגמא - הפונקציה {% equation %}f\left(x\right)=\frac{x^{3}+2x}{x^{2}+7}{% endequation %}:

<img src="{{site.baseurl}}{{site.post_images}}/2022/oblique_asymptote.png" alt=""/>

נראה שבשאיפה לאינסוף הפונקציה הופכת להיות כמעט קו ישר, שכמובן שואף לאינסוף. בואו נראה טריק שיאפשר לי להוכיח ש-{% equation %}g\left(x\right)=x{% endequation %} היא אכן אסימפטוטה: ראשית, שימו לב לכך ש-{% equation %}x^{3}+2x=x\left(x^{2}+7\right)-5x{% endequation %} (עשיתי פה משהו שנקרא <strong>חלוקת פולינומים</strong> ולא קשה יותר מסתם חילוק ארוך אחרי שמתרגלים). כלומר, אני יכול לכתוב

{% equation %}\frac{x^{3}+2x}{x^{2}+7}=\frac{x\left(x^{2}+7\right)-5x}{x^{2}+7}=x-\frac{5x}{x^{2}+7}{% endequation %}

בואו נשווה את הפונקציה הזו לקו הישר {% equation %}g\left(x\right)=x{% endequation %}:

{% equation %}\left|f\left(x\right)-g\left(x\right)\right|=\left|x-\frac{5x}{x^{2}+7}-x\right|=\left|-\frac{5x}{x^{2}+7}\right|{% endequation %}

ואנחנו כבר יודעים שהביטוי הזה שואף לאפס כי המכנה ממעלה גדולה מהמונה.

כדי שהטריק הזה יעבוד, נזקקנו לכך שהמעלה של המונה {% equation %}\frac{x^{3}+2x}{x^{2}+7}{% endequation %} תהיה גדולה מהמעלה של המכנה <strong>בדיוק ב-</strong><strong>1</strong>. אם הייתה פחות גדולה, הייתה לנו אסימפטוטה לא משופעת או שום אסימפטוטה בכלל; ואם הייתה יותר גדולה אז טריק החלוקה של פולינומים היה משאיר אותי עם {% equation %}x^{2}{% endequation %} פחות משהו, או חזקה גבוהה יותר - והיא לא הייתה מתבטלת עם ה-{% equation %}x{% endequation %} של {% equation %}g\left(x\right){% endequation %}.

הדוגמה שנתתי היא קצת מנוונת, כי יוצא שהאסימפטוטה עוברת דרך ראשית הצירים. בואו נראה דוגמא שבה זה לא קורה, אבל לפני כן נבין איך מוצאים אסימפטוטה כזו באופן כללי. נניח שנתונה לנו פונקציה {% equation %}f\left(x\right){% endequation %} ואנחנו רוצים למצוא מה האסימפטוטה ב-{% equation %}x\to\infty{% endequation %} (עבור {% equation %}-\infty{% endequation %} זה יהיה אותו רעיון). בואו נניח שיש אסימפטוטה כזו, {% equation %}g\left(x\right)=mx+a{% endequation %} כך שמתקיים {% equation %}\left|f\left(x\right)-g\left(x\right)\right|\to0{% endequation %}. אני רוצה איכשהו למצוא את {% equation %}m,a{% endequation %}; הנה טריק שיעזור לי לעשות את זה. אם אני לוקח את {% equation %}g\left(x\right){% endequation %} ומחלק אותו ב-{% equation %}x{% endequation %}, התוצאה תהיה {% equation %}\frac{g\left(x\right)}{x}=m+\frac{a}{x}{% endequation %}, והביטוי הזה בבירור שואף ל-{% equation %}m{% endequation %} כאשר {% equation %}x{% endequation %} שואף לאינסוף; אם {% equation %}f\left(x\right){% endequation %} שואפת אל {% equation %}g\left(x\right){% endequation %} כאשר {% equation %}x{% endequation %} שואף לאינסוף אני מצפה שההתנהגות של {% equation %}\frac{f\left(x\right)}{x}{% endequation %} תהיה דומה וגם הוא ישאף אל {% equation %}m{% endequation %}. 

כדי להוכיח פורמלית ש-{% equation %}\lim_{x\to\infty}\frac{f\left(x\right)}{x}=m{% endequation %} אנחנו צריכים לקחת {% equation %}\varepsilon>0{% endequation %} ולהראות שקיים {% equation %}M>0{% endequation %} כך שאם {% equation %}x>M{% endequation %} אז {% equation %}\left|\frac{f\left(x\right)}{x}-m\right|<\varepsilon{% endequation %}. לצורך כך, אני אשתמש בטכניקת הוכחה סופר-נפוצה בחדו"א: אני אפרק את הביטוי {% equation %}\left|\frac{f\left(x\right)}{x}-m\right|{% endequation %} לסכום של <strong>שני</strong> ביטויים, שאת שניהם אני יכול לחסום. אני אעשה את זה עם הטריק של לחבר ולחסר את {% equation %}\frac{g\left(x\right)}{x}{% endequation %} בתוך הביטוי, מה שנותן לי

{% equation %}\left|\frac{f\left(x\right)}{x}-m\right|=\left|\frac{f\left(x\right)}{x}-\frac{g\left(x\right)}{x}+\frac{g\left(x\right)}{x}-m\right|{% endequation %}

ועכשיו אני אשתמש בכלי המרכזי של החדו"א: <strong>אי שוויון המשולש</strong>. זו הטענה שמתקיים {% equation %}\left|A+B\right|\le\left|A\right|+\left|B\right|{% endequation %}. למה קוראים לו ככה ואיפה המשולש פה - ובכן, שולי הפוסט הזה צרים מלהיכנס לזה. אני פשוט אשתמש בו:

{% equation %}\left|\frac{f\left(x\right)}{x}-\frac{g\left(x\right)}{x}+\frac{g\left(x\right)}{x}-m\right|\le\left|\frac{f\left(x\right)}{x}-\frac{g\left(x\right)}{x}\right|+\left|\frac{g\left(x\right)}{x}-m\right|{% endequation %}

כדי לחסום כל ביטוי בנפרד, בואו נזכור אילו גבולות כבר יש לנו:

{% equation %}\lim_{x\to\infty}\left|f\left(x\right)-g\left(x\right)\right|=0{% endequation %}

{% equation %}\lim_{x\to\infty}\frac{g\left(x\right)}{x}=m{% endequation %}

כדי "להפעיל" גבול אני בוחר אפסילון כלשהו ומקבל בחזרה {% equation %}M{% endequation %} כך שאם {% equation %}x>M{% endequation %} אז הפונקציה קרובה לגבול עד כדי אפסילון. לי, כזכור, יש כבר {% equation %}\varepsilon{% endequation %} שהוא ה"אתגר" שאני צריך לענות עליו כשאני מוכיח ש-{% equation %}\lim_{x\to\infty}\frac{f\left(x\right)}{x}=m{% endequation %}, אז אני יכול לבחור את מה להעביר לשני הגבולות הללו בצורה שתתאים לי. מכיוון שאני הולך לחבר את שניהם, אני רוצה שהסכום הכולל שלהם יהיה קטן מ-{% equation %}\varepsilon{% endequation %}, אז אני אוכל לנסות להקטין אותם כך ששניהם קטנים מ-{% equation %}\frac{\varepsilon}{2}{% endequation %}.

הגבול הראשון נותן לי קיום של {% equation %}M_{1}{% endequation %} כך שאם {% equation %}x>M_{1}{% endequation %} אז {% equation %}\left|f\left(x\right)-g\left(x\right)-0\right|<\frac{\varepsilon}{2}{% endequation %}.

הגבול השני נותן לי קיום של {% equation %}M_{2}{% endequation %} כך שאם {% equation %}x>M_{2}{% endequation %} אז {% equation %}\left|\frac{g\left(x\right)}{x}-m\right|<\frac{\varepsilon}{2}{% endequation %}.

עכשיו מגיע תעלול סטנדרטי: אני <strong>אגדיר</strong> {% equation %}M=\max\left\{ M_{1},M_{2}\right\} {% endequation %} וכעת אם {% equation %}x>M{% endequation %} אז הוא בו זמנית גדול מ-{% equation %}M_{1},M_{2}{% endequation %} ולכן שני אי השוויונים למעלה מתקיימים עבורו בו זמנית.

יש סיבוך טכני אחד קטן: אני צריך שיתקיים {% equation %}\left|\frac{f\left(x\right)-g\left(x\right)}{x}\right|<\frac{\varepsilon}{2}{% endequation %}, אבל מה שיש לי הוא {% equation %}\left|f\left(x\right)-g\left(x\right)\right|<\frac{\varepsilon}{2}{% endequation %}. למרבה המזל, אם {% equation %}x>1{% endequation %} אז {% equation %}\left|\frac{f\left(x\right)-g\left(x\right)}{x}\right|<\left|f\left(x\right)-g\left(x\right)\right|<\frac{\varepsilon}{2}{% endequation %} וזה מה שאני רוצה - אבל בשביל זה אני חייב לדרוש שיתקיים {% equation %}x>1{% endequation %}. למרבה השמחה אני באמת שולט על זה - במקום להגדיר {% equation %}M=\max\left\{ M_{1},M_{2}\right\} {% endequation %} אני אגדיר {% equation %}M=\max\left\{ M_{1},M_{2},1\right\} {% endequation %} ואקבל את מה שרציתי.

אם כן, לסיכום:

{% equation %}\left|\frac{f\left(x\right)}{x}-m\right|\le\left|\frac{f\left(x\right)}{x}-\frac{g\left(x\right)}{x}\right|+\left|\frac{g\left(x\right)}{x}-m\right|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon{% endequation %}

זה מה שרציתי להוכיח.

אם כן, בהינתן פונקציה {% equation %}f\left(x\right){% endequation %} שיש לה אסימפטוטה משופעת {% equation %}mx+a{% endequation %} ב-{% equation %}x\to\infty{% endequation %} גילינו איך למצוא את השיפוע {% equation %}m{% endequation %} שלה. אבל איך מוצאים את {% equation %}a{% endequation %}? ובכן, המשמעות של זה ש-{% equation %}mx+a{% endequation %} היא אסימפטוטה של {% equation %}f\left(x\right){% endequation %} הוא שמתקיים {% equation %}\left|f\left(x\right)-mx-a\right|\to0{% endequation %} אם חושבים על ההגדרה רגע רואים שזה אותו הדבר כמו לומר {% equation %}\left|f\left(x\right)-mx\right|\to a{% endequation %}, לכן כל מה שצריך לעשות הוא לחשב גם את הגבול הזה וסיימנו למצוא את האסימפטוטה.

אם לא קיימת אסימפטוטה, האם חישובי הגבולות שהצגתי עדיין יכולים "בטעות" לתת לנו אסימפטוטה שלא קיימת? ובכן, לא. ייתכן שאין אסימפטוטה אבל החישוב של {% equation %}\lim_{x\to\infty}\frac{f\left(x\right)}{x}{% endequation %} יניב איזה גבול {% equation %}m{% endequation %}, זה בהחלט יכול לקרות. אבל אם הגבול {% equation %}\left|f\left(x\right)-mx\right|{% endequation %} קיים ושווה {% equation %}a{% endequation %} זה מוכיח ש-{% equation %}\left|f\left(x\right)-mx-a\right|\to0{% endequation %} שאומר בדיוק שהקו {% equation %}mx+a{% endequation %} הוא אסימפטוטה של {% equation %}f\left(x\right){% endequation %}. אם לעומת זאת הגבול {% equation %}\left|f\left(x\right)-mx\right|{% endequation %} לא קיים, אז אכן אין אסימפטוטה.

בואו נראה עכשיו דוגמא קונקרטית - הפונקציה {% equation %}f\left(x\right)=\frac{2x^{2}+3x+1}{x}{% endequation %}. ראשית, {% equation %}\frac{f\left(x\right)}{x}=\frac{2x^{2}+3x+1}{x^{2}}\to2{% endequation %} (זה הטריק הרגיל של מנת המקדמים המובילים של המונה והמכנה) אז {% equation %}m=2{% endequation %}. 

שנית, {% equation %}f\left(x\right)-mx=\frac{2x^{2}+3x+1}{x}-2x=\frac{3x+1}{x}{% endequation %} ולכן {% equation %}\left|f\left(x\right)-mx\right|\to3{% endequation %}, וקיבלנו את האסימפטוטה {% equation %}y=2x+3{% endequation %}.

כאן אני הולך לעצור - כיסינו את המושגים הבסיסיים וקצת את האופן שבו משתמשים בהם, אבל עם דוגמאות וטכניקות קונקרטיות לחישוב אסימפטוטות בסיטואציות שונות ומשונות - עם זה אפשר להמשיך עד אינסוף. 